import wx
import time
import threading
import base64
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
from mail.packet import Packet, Agent

# Local database directory
dbdir = "data/"
# GPG data directory
gpgdir = "data/gnupg"
# GPG binary
gpgbinary = "gpg2"
# Local database file extension
dbext = ".db.sqlite"
# The user information file
infopath = "info.txt"
# Wating time for receiving email thread
waiting_time = 5
# Verbose option of GPG
# You may find it quite useful, when your GPG
# doesn't work correctly
gpgverbose = False

#注册窗口
class SignupFrame(SignupFrameMod):

    def __init__(self, parent, verbose=True):
        super().__init__(parent)
        self.verbose = verbose
        self.keyid = None
    #确认是否已经注册成功，未成功时显示失败窗口
    def check_signup(self):
        if not SignupFrameMod.check_signup(self):
            return False
        result, message = mail.check_smtp_info(self.mail, self.password, self.server)
        if not result:
            dlg = wx.MessageDialog(self, message, "Failure", wx.OK)
            dlg.ShowModal()
            return False

        self.keyid = ''
        # self.keyid = str(gpg.gen_key(self.name, self.mail, self.password))
        return True
    #开启lock窗口
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

#lock窗口
class LockFrame(LockFrameMod):
    #设置数据库路径
    def set_db_path(self):
        self.info.dbpath = dbdir + self.info.mail + dbext
    #初始化数据库
    def init_db(self):
        self.set_db_path()
        init_db(self.info.dbpath)
    #加密本地数据库文件
    def encrypt_db(self):
        self.info.salt = fernet.encrypt_file(self.lock, self.info.dbpath)
    #密码生成并存入本地数据库
    def encrypt_password(self):
        self.info.password = fernet.encrypt_string(self.lock,
                                                   self.info.salt, self.info.realpassword)
    #信息写入数据库
    def write_info(self):
        self.info.write(infopath)

    def print_info(self):
        self.info.print()
    #解密本地数据库文件
    def decrypt_file(self):
        return fernet.decrypt_file(self.lock, self.info.salt, self.info.dbpath)
    #对本地数据库中的密码进行解密
    def decrypt_password(self):
        self.info.realpassword = \
            fernet.decrypt_string(self.lock, self.info.salt, self.info.password)
    #设置lock
    def set_lock(self):
        if (self.verbose):
            print("Setting up the lock")
        self.init_db()
        self.encrypt_db()
        self.encrypt_password()
        self.set_up_gpg()

        self.write_info()

        return True
    #确认lock
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
    #输入lock后显示的窗口
    def start_has_lock_frame(self):
        frame = self.__class__(None, LockDialogType.HASLOCK,
                             self.lock, self.verbose)
        frame.info = self.info
        frame.Show()
    #未输入lock后显示的窗口
    def start_no_lock_frame(self):
        frame = self.__class__(None, LockDialogType.NOLOCK,
                               None, self.verbose)
        frame.info = self.info
        frame.Show()
    #显示主窗口
    def strat_main_frame(self):
        if (self.verbose):
            print("Starting main frame")
        frame = MainFrame(None, info=self.info)
        frame.info = self.info
        frame.Show()
    #设置gpg加密
    def set_up_gpg(self):
        gpg = GPG(binary=gpgbinary, homepath=gpgdir, verbose=gpgverbose)
        print("reallock=", self.lock)
        self.info.keyid = str(gpg.gen_key(self.info.name, self.info.mail, self.lock))

#主窗口类
class MainFrame(MainFrameMod):
     #主窗口中存在的对象
    def __init__(self, parent, info=None):
        MainFrameMod.__init__(self, parent)
        self.info = info
        self.SetTitle('GPGChat (' + self.info.mail + ' | ' + self.info.name + ' | ' + self.info.keyid + ')')
        self.uuid = uuid4()
        self.seqmap = {}
        self.DisableInput()
        self.current_keyid = None
        self.current_mail = None
        self.gpg = GPG(binary=gpgbinary, homepath=gpgdir, verbose=gpgverbose)
        self.contactCanBeRead = True
        self.OnContactButton(None)

        self.start_listern_thread()
    #发送信息获取
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
            # self.update_last_message_time()
    #为每个keyid添加sequence
    def increment_seq(self, keyid):
        if not keyid in self.seqmap:
            self.seqmap[keyid] = 0
        else:
            self.seqmap[keyid] = self.seqmap[keyid] + 1
        return self.seqmap[keyid]
    #由输入窗口将需要发送的信息写入数据库
    def add_sent_message_to_db(self, text, keyid):
        db.add_massage(db_path=self.info.dbpath,
                       uuid=self.uuid,
                       seq=self.seqmap[keyid],
                       send_from=None,
                       send_to=keyid,
                       content=text,
                       timestamp=time.time())
    #确认发送的信息是否为空
    def check_text(self, text):
        if text is None or text == '':
            self.show_dialog('Text cannot be empty!', 'Warning')
            return False
        return True
    #确认是否选择发送的联系人
    def check_contact_selected(self):
        if self.blacklistDisplayed:
            self.show_dialog('You haven\'t selected any contact yet!', 'Warning')
            return False
        return True
    #联系人选择操作
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
    #显示双方对话
    def show_dialog(self, message, title):
        dlg = wx.MessageDialog(self, message,
                               title,
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
    #信息的相关处理，加密
    def send_text(self, text):
        # self.show_dialog('Cannot connect to the SMTP server', 'Failure')
        connection, message = mail.connect_smtp(self.info.mail, self.info.realpassword, self.info.server)
        if connection is None:
            self.show_dialog(message, 'Failure')
            return False
        text = base64.urlsafe_b64encode(text.encode()).decode()
        print("base64", text)
        text = self.gpg.encrypt(text, self.current_keyid)
        packet = Packet()
        packet.set_message(text)
        packet.set_receiver(self.current_mail)
        packet.set_sender(self.info.mail)
        packet.set_sequence(self.increment_seq(self.current_keyid))
        packet.set_signedkeyid(self.info.keyid)
        packet.set_uuid(str(self.uuid))
        agent = Agent()
        result, message = agent.send_packet(connection, packet)
        # result, message = mail.send_mail(connection, self.info.mail, self.current_mail, text, str(self.uuid))
        if not result:
            self.show_dialog(message, 'Failure')
            return False
        return True
    #从数据库中下载所有信息
    def load_all_messages(self, keyId):
        allmessages = db.fetch_all_messages(self.info.dbpath, keyId)
        for messagelist in allmessages:
            message = self.load_message(messagelist)
            if message.send:
                self.AddSendMessage(str(message))
            else:
                self.AddRecvMessage(str(message))
        # self.m_scrolledWindow1.Scroll(-1, self.GetClientSize()[1])
    #生成信息列表
    def load_message(self, messagelist):
        message = Message()
        message.send = messagelist[0]
        message.text = messagelist[1]
        message.timestamp = messagelist[2]
        message.uuid = messagelist[3]
        message.seq = messagelist[4]
        return message
    #添加联系人操作
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
    #度去联系人信息
    def ReadContactData(self):
        if not self.contactCanBeRead:
            return
        contact_list = db.read_contact(self.info.dbpath)
        self.contact_data = {}
        cnt = 1
        for contact in contact_list:
            self.contact_data[cnt] = contact
            cnt = cnt + 1
    #读取黑名单信息
    def ReadBlacklistData(self):
        if not self.contactCanBeRead:
            return
        blacklist = db.read_contact(self.info.dbpath, status='B')
        self.blacklist_data = {}
        cnt = 1
        for contact in blacklist:
            self.blacklist_data[cnt] = contact
            cnt = cnt + 1
    #更新最近一次发送消息时间
    def update_last_message_time(self):
        self.list.SetItem(self.currentItem, 3, time_to_string(time.time()))
    #删除联系人
    def remove_contact(self, keyid):
        return db.delete_contact(self.info.dbpath, keyid)

    def block_contact(self, keyid):
        return db.alter_contact_block(self.info.dbpath, keyid)
    #连接服务器互通信息
    def listen_mail(self):
        agent = Agent()
        while True:
            # print("Listening for new emails")
            connection = mail.connect_imap(self.info.mail, self.info.realpassword, self.info.imapserver)
            if connection is None:
                self.ShowWarningMessage("Cannot connect to the IMAP Server!")
                break
            packets = agent.receive_packet(connection)
            for packet in packets:
                message = self.gpg.decrypt(packet.message, self.info.reallock)
                message = base64.urlsafe_b64decode(message).decode()
                print("base64", message)
                db.add_massage(self.info.dbpath, packet.uuid,
                               packet.sequence, packet.signed_keyid, None,
                               message, time.time())
                self.ClearAllMessages()
                self.load_all_messages(self.current_keyid)
            time.sleep(5)
    #多线程实现同时收发消息
    def start_listern_thread(self):
        # t = threading.Thread(target=self.listen_mail)
        # t.setDaemon(True)
        #Segmentation fault: t.start()

        myEVT_LISTEN = wx.NewEventType()
        EVT_LISTENING = wx.PyEventBinder(myEVT_LISTEN, 1)
        self.Bind(EVT_LISTENING, self.OnListen)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.listening_thread = ListeningMailsThread(self, myEVT_LISTEN, self.info, self.gpg)
        self.listening_thread.setDaemon(True)
        self.listening_thread.start()
        # t.join()
    #关闭窗口
    def OnClose(self, evt):
        if self.listening_thread is not None:
            self.listening_thread.stop = True
            time.sleep(waiting_time)
        self.Destroy()
    #等待接收信息
    def OnListen(self, evt):
        newmail = evt.isNewmail()
        if newmail:
            self.ClearAllMessages()
            self.load_all_messages(self.current_keyid)


class ListeningEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, newmail=False):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self._newmail = newmail

    def isNewmail(self):
        return self._newmail

class ListeningMailsThread(threading.Thread):
    def __init__(self, parent, etype, info, gpg):
        threading.Thread.__init__(self)
        self._parent = parent
        self._etype = etype
        self.info = info
        self.gpg = gpg
        self.stop = False

    def run(self):
        agent = Agent()
        while not self.stop:
            print("Listening for new emails")
            connection = mail.connect_imap(self.info.mail, self.info.realpassword, self.info.imapserver)
            if connection is None:
                # self.ShowWarningMessage("Cannot connect to the IMAP Server!")
                break
            packets = agent.receive_packet(connection)
            for packet in packets:
                message = self.gpg.decrypt(packet.message, self.info.reallock)
                message = base64.urlsafe_b64decode(message).decode()
                print("base64", message)
                db.add_massage(self.info.dbpath, packet.uuid,
                               packet.sequence, packet.signed_keyid, None,
                               message, time.time())
                evt = ListeningEvent(self._etype, -1, True)
                wx.PostEvent(self._parent, evt)
                # self.ClearAllMessages()
                # self.load_all_messages(self.current_keyid)
            time.sleep(waiting_time)

class AddContactFrame(AddContactFrameMod):
    def __init__(self, parent, gpg):
        AddContactFrameMod.__init__(self, parent)
        self.gpg = gpg
        self.keys = {}

    def StartChooseContactFrame(self):
        self.keysmap = self.gpg.keys_to_datamap(self.keys)
        chooseContactFrame = ChooseContactFrame(self.parent, self.keysmap)
        chooseContactFrame.Show()
    #在gpg加密的情况下搜索用户
    def check_gpg(self):
        self.keys = self.gpg.search(self.email)
        if len(self.keys) == 0:
            self.ShowWarningMessage("Cannot find that user!")
            return False
        return True



class ChooseContactFrame(ChooseContactFrameMod):
    #确认选择该联系人
    def OnConfirmButton( self, event ):
        ChooseContactFrameMod.OnConfirmButton(self, event)

        name = self.list.GetItem(self.currentItem, 0).GetText()
        mail = self.list.GetItem(self.currentItem, 1).GetText()
        keyid = self.list.GetItem(self.currentItem, 2).GetText()
        self.parent.add_contact(name, mail, keyid)
        self.Close()
#APP类
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

#运行gpgchat
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
