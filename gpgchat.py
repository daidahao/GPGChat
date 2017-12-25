import wx
from ui.starter import LockFrameMod, LockDialogType
from encrypt import fernet, info

dbpath = ".db.sqlite"
infopath = "info.txt"
testpath = "test.db"

class LockFrame(LockFrameMod):

    def setlock(self):
        if (self.verbose):
            print("Setting up the lock")
        self.mail = "zou@qq.com"
        self.salt = fernet.encrypt(self.lock, testpath)
        info.writeinfo(self.mail, self.salt, infopath)
        return True

    def islockcorrect(self):
        if (self.verbose):
            print("Checking if the lock is correct")
        if fernet.decrypt(self.lock, self.salt, testpath) == False:
            print("The lock is incorrect!")
            return False
        print("The lock is correct!")
        return True

    def starthaslockframe(self):
        frame = self.__class__(None, LockDialogType.HASLOCK,
                             self.lock, self.verbose)
        frame.salt = self.salt
        frame.Show()


if __name__ == '__main__':
    app = wx.App()
    inf = info.readinfo(infopath)
    if inf == False:
        frame = LockFrame(None, LockDialogType.NOLOCK, verbose=True)
    else:
        frame = LockFrame(None, LockDialogType.HASLOCK, verbose=True)
        frame.mail = inf[0]
        frame.salt = inf[1]
    frame.Show()
    app.MainLoop()
