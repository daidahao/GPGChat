from ui import SignupFrame, MainFrame, LockFrame
import wx
import time


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

class LockFrameMod(LockFrame):
    def __init__(self, parent,
                 type=LockDialogType.NOLOCK, lock=None, verbose=False):

        LockFrame.__init__(self, parent)
        self.type = type
        self.lock = lock
        self.verbose = verbose

        if self.verbose:
            print("Initializing LockDialog")

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
                    # dlg.Destroy()

                    frame = LockFrameMod(None, LockDialogType.HASLOCK,
                                         self.lock, self.verbose)
                    frame.Show()

                    self.Close()
                else:
                    dlg = wx.MessageDialog(self,
                                           "The confirmed lock is inconsistent with the "
                                           "previous one. Please try again!",
                                           "Failure", wx.OK)
                    dlg.ShowModal()
                    # dlg.Destroy()

                    frame = LockFrameMod(None)
                    frame.Show()

                    self.Close()
        else:
            self.lock = self.lockText.GetValue()
            if (self.lock == "123"):
                # frame = SignupFrameMod(None)
                # frame.Show()
                # self.Destroy()
                frame = MainFrameMod(None)
                frame.Show()
                self.Close()
            else:
                dlg = wx.MessageDialog(self,
                                       "Your lock is incorrect!",
                                       "Failure", wx.OK)
                dlg.ShowModal()
                # dlg.Destroy()

                frame = LockFrameMod(None, LockDialogType.HASLOCK)
                frame.Show()

                self.Close()

            # self.Destroy()



data1 = {
    1: ("Dai", "daidahao@icloud.com", "9999999", time.time()),
    2: ("Zou", "999@test.com", "9999999", time.time() - 3600),
    3: ("Sun", "test@test.com", "9999999", time.time() + 36000),
}

def time_to_string(t):
    t_localtime = time.localtime(t)
    localtime = time.localtime()
    if (t_localtime.tm_year == localtime.tm_year
        and t_localtime.tm_mon == localtime.tm_mon
        and t_localtime.tm_mday == localtime.tm_mday):
        return time.strftime("%H:%M:%S", t_localtime)
    return time.strftime("%Y-%m-%d %H:%M:%S", t_localtime)

class MainFrameMod(MainFrame):

    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        self.PopulateList()
        self.count = 0
        self.allText = []

    def PopulateList(self):

        # for normal, simple columns, you can add them like this:
        self.list.InsertColumn(0, "Email")
        self.list.InsertColumn(1, "Name")
        self.list.InsertColumn(2, "KeyID")
        self.list.InsertColumn(3, "Last Message")
        items = data1.items()
        for key, data in items:
            index = self.list.InsertItem(self.list.GetItemCount(), data[0])
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2 ,data[2])
            self.list.SetItem(index, 3, time_to_string(data[3]))
            self.list.SetItemData(index, key)

        self.list.SetColumnWidth(0, 50)
        self.list.SetColumnWidth(1, 100)
        self.list.SetColumnWidth(2, 100)
        self.list.SetColumnWidth(3, 150)

        self.currentItem = 0

    def OnSend( self, event ):
        self.AddSendMessage(self.inputText.GetValue())

    def AddSendMessage(self, message):
        self.AddMessage(send=True, message=message)

    def AddRecvMessage(self, message):
        self.AddMessage(send=False, message=message)

    def AddMessage(self, send=True, message=""):
        wrapSizer = self.m_scrolledWindow1.GetSizer()
        self.count = self.count + 1

        textCtrl = wx.StaticText(self.m_scrolledWindow1, wx.ID_HIGHEST + 1, u"", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        textCtrl.SetLabelText(message)
        textCtrl.Wrap(250)
        textCtrl.SetForegroundColour(wx.Colour(255, 255, 255))
        textCtrl.SetBackgroundColour(wx.Colour(0, 128, 255))

        if (send):
            wrapSizer.Add(textCtrl, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        else:
            wrapSizer.Add(textCtrl, 0, wx.ALL | wx.ALIGN_LEFT, 5)


        self.m_scrolledWindow1.SetSizerAndFit(wrapSizer)
        self.m_scrolledWindow1.Layout()
        self.m_panel15.Layout()


if __name__ == '__main__':
    app = wx.App()
    # dialog = LockDialogMod(None)
    # dialog.Show()
    frame = LockFrameMod(None)
    frame.Show()
    app.MainLoop()
