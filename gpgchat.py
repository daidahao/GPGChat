import wx

from encrypt import fernet
from info import Info
from ui.starter import LockFrameMod, LockDialogType, SignupFrameMod
from database.init_db import init_db
from util.file import write_file, rm_file

dbdir = "data/"
dbext = ".db.sqlite"
infopath = "info.txt"
testpath = "test.db"


class SignupFrame(SignupFrameMod):
    def checksignup(self):
        if not SignupFrameMod.checksignup(self):
            return False
        return True

    def startlockframe(self):
        frame = LockFrame(None, LockDialogType.NOLOCK, verbose=True)
        frame.info = self.setinfo()
        frame.Show()
        self.Close()

    def setinfo(self):
        info = Info()
        info.mail = self.mail
        info.name = self.name
        info.realpassword = self.password
        info.server = self.server
        return info

class LockFrame(LockFrameMod):

    def setlock(self):
        if (self.verbose):
            print("Setting up the lock")
        self.info.dbpath = dbdir + self.info.mail + dbext
        init_db(self.info.dbpath)
        self.info.salt = fernet.encrypt(self.lock, self.info.dbpath)
        self.info.password = fernet.encryptstring(self.lock,
                                                  self.info.salt, self.info.realpassword)
        self.info.write(infopath)

        return True

    def islockcorrect(self):
        self.info.print()
        if (self.verbose):
            print("Checking if the lock is correct")
        dec = fernet.decrypt(self.lock, self.info.salt, self.info.dbpath)
        if dec == False:
            print("The lock is incorrect!")
            return False
        write_file(self.info.dbpath, dec)
        if (self.verbose):
            print("The lock is correct!")
        self.info.realpassword = fernet.decryptstring(self.lock,
                                                     self.info.salt,
                                                     self.info.password)
        self.info.print()
        return True

    def starthaslockframe(self):
        frame = self.__class__(None, LockDialogType.HASLOCK,
                             self.lock, self.verbose)
        frame.info = self.info
        frame.Show()


if __name__ == '__main__':
    app = wx.App()
    info = Info()

    if info.read(infopath) == False:
        frame = SignupFrame(None)
    else:
        frame = LockFrame(None, LockDialogType.HASLOCK, verbose=True)
        frame.info = info

    frame.Show()
    app.MainLoop()
