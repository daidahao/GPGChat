import wx

from encrypt import fernet
from info import Info
from ui.starter import LockFrameMod, LockDialogType, SignupFrameMod, MainFrameMod
from database.init_db import init_db
from util.file import write_file, rm_file

dbdir = "data/"
dbext = ".db.sqlite"
infopath = "info.txt"
testpath = "test.db"


class SignupFrame(SignupFrameMod):


    def __init__(self, parent, verbose=True):
        super().__init__(parent)
        self.verbose = verbose

    def check_signup(self):
        if not SignupFrameMod.check_signup(self):
            return False
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
        return info


class LockFrame(LockFrameMod):

    def set_db_path(self):
        self.info.dbpath = dbdir + self.info.mail + dbext

    def init_db(self):
        self.set_db_path()
        init_db(self.info.dbpath)

    def encrypt_db(self):
        self.info.salt = fernet.encrypt(self.lock, self.info.dbpath)

    def encrypt_password(self):
        self.info.password = fernet.encryptstring(self.lock,
                                                  self.info.salt, self.info.realpassword)

    def write_info(self):
        self.info.write(infopath)

    def print_info(self):
        self.info.print()

    def decrypt_file(self):
        return fernet.decrypt(self.lock, self.info.salt, self.info.dbpath)

    def decrypt_password(self):
        self.info.realpassword = \
            fernet.decryptstring(self.lock, self.info.salt, self.info.password)

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

    def strat_main_frame(self):
        if (self.verbose):
            print("Starting main frame")
        frame = MainFrame(None)
        frame.Show()

class MainFrame(MainFrameMod):
    pass


class GPGApp(wx.App):

    def write_info(self):
        if self.info.salt is None:
            return
        self.info.write(infopath)

    def encrypt_password(self):
        if self.info.salt or self.info.realpassword is None:
            return
        self.info.password = fernet.encryptstring(self.info.reallock,
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
            self.info.salt = fernet.encrypt(self.info.reallock, self.info.dbpath)



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
