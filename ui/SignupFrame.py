from ui import SignupFrame, LockDialog
import wx

class SignupFrame(SignupFrame):
    def OnSignup(self, event):
        dlg = wx.MessageDialog(self,
                               "Signup successfully!",
                               "Success",
                               wx.OK)
        dlg.Center()
        dlg.ShowModal()
        dlg.Destroy()

class LockDialogMod(LockDialog):
    def __init__(self, parent, noLock=True):
        LockDialog.__init__(self, parent)
        if (noLock):
            pass

    def OnLockButton(self, event):
        event.skip()


if __name__ == '__main__':
    app = wx.App()
    frm = LockDialogMod(None)
    frm.Show()
    app.MainLoop()