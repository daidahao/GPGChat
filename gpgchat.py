import wx
from ui.starter import LockFrameMod
from encrypt import fernet

dbpath = "db.sqlite"

class LockFrame(LockFrameMod):

    def setlock(self):
        if (self.verbose):
            print("Setting up the lock")
        fernet.encrypt(self.lock, dbpath)
        return True

    def islockcorrect(self):
        if (self.verbose):
            print("Checking if the lock is correct")
        if fernet.decrypt(self.lock, dbpath) == False:
            print("The lock is incorrect!")
            return False
        print("The lock is correct!")
        return True


if __name__ == '__main__':
    app = wx.App()
    frame = LockFrame(None, verbose=True)
    frame.Show()
    app.MainLoop()
