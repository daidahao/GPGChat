import wx
import time
from uuid import uuid4

from encrypt import fernet
from encrypt.gpg import GPG
from info import Info
from ui.starter import LockFrameMod, LockDialogType, SignupFrameMod, MainFrameMod, AddContactFrameMod, ChooseContactFrameMod, time_to_string
from database.init_db import init_db
from database import db
from util.file import write_file
from mail import mail
from model.message import Message

dbdir = "data/"
gpgdir = "data/gnupg"
gpgbinary = "gpg2"
dbext = ".db.sqlite"
infopath = "info.txt"
testpath = "test.db"


class SignupFrame(SignupFrameMod):

    def __init__(self, parent, verbose=True):
        super().__init__(parent)
        self.verbose = verbose
        self.keyid = None

    def check_signup(self):
        if not SignupFrameMod.check_signup(self):
            return False
        result, message = mail.check_smtp_info(self.mail, self.password, self.server)
        if not result:
            dlg = wx.MessageDialog(self, message, "Failure", wx.OK)
            dlg.ShowModal()
            return False
        gpg = GPG(binary=gpgbinary, homepath=gpgdir)
        self.keyid = str(gpg.gen_key(self.name, self.mail, self.password))
        return True

    def start_lock_frame(self):
        frame = LockFrame(None, LockDialogType.NOLOCK, verbose=self.verbose)
        frame.info = self.setinfo()
        frame.Show()
        self.Close()

    def setinfo(self):
        # info = Info()
        info.mail = self.mail
        info.name = self.name
        info.realpassword = self.password
        info.server = self.server
        info.imapserver = self.imapserver
        info.keyid = self.keyid
        return info


class LockFrame(LockFrameMod):

    def set_db_path(self):
        self.info.dbpath = dbdir + self.info.mail + dbext

    def init_db(self):
        self.set_db_path()
        init_db(self.info.dbpath)

    def encrypt_db(self):
        self.info.salt = fernet.encrypt_file(self.lock, self.info.dbpath)

    def encrypt_password(self):
        self.info.password = fernet.encrypt_string(self.lock,
                                                   self.info.salt, self.info.realpassword)

    def write_info(self):
        self.info.write(infopath)

    def print_info(self):
        self.info.print()

    def decrypt_file(self):
        return fernet.decrypt_file(self.lock, self.info.salt, self.info.dbpath)

    def decrypt_password(self):
        self.info.realpassword = \
            fernet.decrypt_string(self.lock, self.info.salt, self.info.password)

    def set_lock(self):
        if (self.verbose):
            print("Setting up the lock")
        self.init_db()
        self.encrypt_db()
        self.encrypt_password()
        self.write_info()
        return True

    def is_lock_correct(self):
        if (self.verbose):
            print("Checking if the lock is correct")
        dec = self.decrypt_file()
        if dec == False:
            if (self.verbose):
                print("The lock is incorrect!")
            return False
        write_file(self.info.dbpath, dec)
        if (self.verbose):
            print("The lock is correct!")
        self.decrypt_password()
        self.print_info()
        self.info.reallock = self.lock
        return True

    def start_has_lock_frame(self):
        frame = self.__class__(None, LockDialogType.HASLOCK,
                             self.lock, self.verbose)
        frame.info = self.info
        frame.Show()

    def start_no_lock_frame(self):
        frame = self.__class__(None, LockDialogType.NOLOCK,
                               None, self.verbose)
        frame.info = self.info
        frame.Show()

    def strat_main_frame(self):
        if (self.verbose):
            print("Starting main frame")
        frame = MainFrame(None, info=self.info)
        frame.info = self.info
        frame.Show()

class MainFrame(MainFrameMod):

    def __init__(self, parent, info=None):
        MainFrameMod.__init__(self, parent)
        self.info = info
        self.SetTitle('GPGChat (' + self.info.mail + ' | ' + self.info.name + ' | ' + self.info.keyid + ')')
        self.uuid = uuid4()
        self.seqmap = {}
        self.DisableInput()
        self.current_keyid = None
        self.current_mail = None
        self.gpg = GPG(binary=gpgbinary, homepath=gpgdir)
        self.contactCanBeRead = True
        self.OnContactButton(None)

    def OnSend( self, event ):
        text = self.inputText.GetValue()
        self.DisableInput()
        if (not self.check_text(text)) or (not self.check_contact_selected()):
            self.EnableInput()
            return
        if self.send_text(text):
            self.add_sent_message_to_db(text, self.current_keyid)
            self.ClearAllMessages()
            self.load_all_messages(self.current_keyid)
            self.EnableInput()
            self.inputText.SetValue('')
            self.update_last_message_time()

    def increment_seq(self, keyid):
        if not keyid in self.seqmap:
            self.seqmap[keyid] = 0
        else:
            self.seqmap[keyid] = self.seqmap[keyid] + 1
        return self.seqmap[keyid]

    def add_sent_message_to_db(self, text, keyid):
        db.add_massage(db_path=self.info.dbpath,
                       uuid=self.uuid,
                       seq=self.increment_seq(keyid),
                       send_from=None,
                       send_to=keyid,
                       content=text,
                       timestamp=time.time())

    def check_text(self, text):
        if text is None or text == '':
            self.show_dialog('Text cannot be empty!', 'Warning')
            return False
        return True

    def check_contact_selected(self):
        if self.blacklistDisplayed:
            self.show_dialog('You haven\'t selected any contact yet!', 'Warning')
            return False
        return True

    def OnItemSelected(self, event):
        self.currentItem = event.Index
        self.current_mail = self.list.GetItem(self.currentItem, 1).GetText()
        self.current_keyid = self.list.GetItem(self.currentItem, 2).GetText()
        self.ClearAllMessages()
        self.load_all_messages(self.current_keyid)
        if not self.blacklistDisplayed:
            self.EnableInput()
        else:
            self.DisableInput()

    def show_dialog(self, message, title):
        dlg = wx.MessageDialog(self, message,
                               title,
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()

    def send_text(self, text):
        # self.show_dialog('Cannot connect to the SMTP server', 'Failure')
        connection, message = mail.connect_smtp(self.info.mail, self.info.realpassword, self.info.server)
        if connection is None:
            self.show_dialog(message, 'Failure')
            return False
        result, message = mail.send_mail(connection, self.info.mail, self.current_mail, text, str(self.uuid))
        if not result:
            self.show_dialog(message, 'Failure')
            return False
        return True

    def load_all_messages(self, keyId):
        allmessages = db.fetch_all_messages(self.info.dbpath, keyId)
        for messagelist in allmessages:
            message = self.load_message(messagelist)
            if message.send:
                self.AddSendMessage(str(message))
            else:
                self.AddRecvMessage(str(message))
        # self.m_scrolledWindow1.Scroll(-1, self.GetClientSize()[1])

    def load_message(self, messagelist):
        message = Message()
        message.send = messagelist[0]
        message.text = messagelist[1]
        message.timestamp = messagelist[2]
        message.uuid = messagelist[3]
        message.seq = messagelist[4]
        return message

    def StartAddContactFrame(self):
        addContactFrame = AddContactFrame(self, self.gpg)
        addContactFrame.Show()

    def add_contact(self, name, mail, keyid):
        if not db.add_contact(self.info.dbpath, name, mail, keyid):
            self.ShowWarningMessage("Cannot add that user!")
            return
        else:
            self.ShowSuccessMessage("Add contact successfully")
            self.OnContactButton(None)

    def ReadContactData(self):
        if not self.contactCanBeRead:
            return
        contact_list = db.read_contact(self.info.dbpath)
        self.contact_data = {}
        cnt = 1
        for contact in contact_list:
            self.contact_data[cnt] = contact
            cnt = cnt + 1

    def ReadBlacklistData(self):
        if not self.contactCanBeRead:
            return
        blacklist = db.read_contact(self.info.dbpath, status='B')
        self.blacklist_data = {}
        cnt = 1
        for contact in blacklist:
            self.blacklist_data[cnt] = contact
            cnt = cnt + 1

    def update_last_message_time(self):
        self.list.SetItem(self.currentItem, 3, time_to_string(time.time()))

    def remove_contact(self, keyid):
        return db.delete_contact(self.info.dbpath, keyid)

    def block_contact(self, keyid):
        return db.alter_contact_block(self.info.dbpath, keyid)


class AddContactFrame(AddContactFrameMod):
    def __init__(self, parent, gpg):
        AddContactFrameMod.__init__(self, parent)
        self.gpg = gpg
        self.keys = {}

    def StartChooseContactFrame(self):
        self.keysmap = self.gpg.keys_to_datamap(self.keys)
        chooseContactFrame = ChooseContactFrame(self.parent, self.keysmap)
        chooseContactFrame.Show()


    def check_gpg(self):
        self.keys = self.gpg.search(self.email)
        if len(self.keys) == 0:
            self.ShowWarningMessage("Cannot find that user!")
            return False
        return True



class ChooseContactFrame(ChooseContactFrameMod):

    def OnConfirmButton( self, event ):
        ChooseContactFrameMod.OnConfirmButton(self, event)

        name = self.list.GetItem(self.currentItem, 0).GetText()
        mail = self.list.GetItem(self.currentItem, 1).GetText()
        keyid = self.list.GetItem(self.currentItem, 2).GetText()
        self.parent.add_contact(name, mail, keyid)
        self.Close()

class GPGApp(wx.App):

    def write_info(self):
        if self.info.salt is None:
            return
        self.info.write(infopath)

    def encrypt_password(self):
        if self.info.salt is None or self.info.realpassword is None:
            return
        self.info.password = fernet.encrypt_string(self.info.reallock,
                                                   self.info.salt, self.info.realpassword)

    def OnExit(self):
        print("OnExit:")
        self.encrypt_db()
        # self.remove_db()
        self.encrypt_password()
        self.write_info()
        return super().OnExit()

    # def remove_db(self):
    #     if self.info.dbpath is not None:
    #         print("Removing the decrypted database file...")
    #         rm_file(self.info.dbpath)

    def encrypt_db(self):
        if self.info.reallock is not None and self.info.dbpath is not None:
            print("Encrypting the database file again...")
            self.info.salt = fernet.encrypt_file(self.info.reallock, self.info.dbpath)


if __name__ == '__main__':
    info = Info()
    app = GPGApp()
    app.info = info

    if info.read(infopath) == False:
        frame = SignupFrame(None, verbose=True)
        frame.info = info
    else:
        frame = LockFrame(None, LockDialogType.HASLOCK, verbose=True)
        frame.info = info

    frame.Show()
    app.MainLoop()
