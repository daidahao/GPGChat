from ui import SignupFrame, LockDialog
import wx

class SignupFrameMod(SignupFrame):
    def OnSignup(self, event):
        dlg = wx.MessageDialog(self,
                               "Signup successfully!",
                               "Success",
                               wx.OK)
        dlg.Center()
        dlg.ShowModal()
        dlg.Destroy()

    def OnQuit(self, event):
        self.Destroy()

class LockDialogType:
    NOLOCK, HASLOCK = range(2)

class LockDialogMod(LockDialog):
    def __init__(self, parent,
                 type=LockDialogType.NOLOCK, lock=None):

        LockDialog.__init__(self, parent)

        self.type = type
        self.lock = lock

        if (type == LockDialogType.NOLOCK):
            self.lockLabel.SetLabelText("Please set your lock first")
            self.lockButton.SetLabelText("Set")



    def OnLockButton(self, event):
        if (self.type == LockDialogType.NOLOCK):
            if (self.lock == None):
                self.lock = self.lockText.GetValue()
                self.lockText.SetValue("")
                self.lockLabel.SetLabelText("Please confirm your lock")
                self.lockButton.SetLabelText("Confirm")
            else:
                if (self.lock == self.lockText.GetValue()):
                    dlg = wx.MessageDialog(self,
                                           "Your lock is set successfully!",
                                           "Success", wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()

                    dialog = LockDialogMod(None, True)
                    dialog.Show()

                    self.Destroy()
                else:
                    dlg = wx.MessageDialog(self,
                                           "The confirmed lock is inconsistent with the previous one, please try again!",
                                           "Failure", wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()

                    dialog = LockDialogMod(None)
                    dialog.Show()

                    self.Destroy()
        else:
            self.lock = self.lockText.GetValue()
            if (self.lock == "123"):
                frame = SignupFrameMod(None)
                frame.Show()
                self.Destroy()
            else:
                dlg = wx.MessageDialog(self,
                                       "Your lock is incorrect!",
                                       "Failure", wx.OK)
                dlg.ShowModal()
                dlg.Destroy()

                dialog = LockDialogMod(None, True)
                dialog.Show()

            self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    dialog = LockDialogMod(None)
    dialog.Show()
    app.MainLoop()