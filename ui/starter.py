
import wx

class SigninFrame(wx.Frame):
    def __init__(self, parent, ID=wx.ID_ANY, title="Signin to GPGChat",
                 pos=wx.DefaultPosition,
                 size=(500, 400), style=wx.DEFAULT_FRAME_STYLE):
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        self.Center()

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.AddSpacer(10)

        label = wx.StaticText(panel, -1, "SIGNIN")
        font = label.GetFont()
        font.PointSize += 20
        label.SetFont(font)
        sizer.Add(label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.AddSpacer(15)

        # Email

        emailSizer = wx.BoxSizer(wx.HORIZONTAL)
        emailLabel = wx.StaticText(panel, -1, "E-mail",
                                   size=(195, -1), style=wx.ALIGN_RIGHT)
        emailSizer.Add(emailLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        emailSizer.AddSpacer(5)

        emailText = wx.TextCtrl(panel, -1, "", size=(200, -1))
        emailSizer.Add(emailText, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.Add(emailSizer, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        sizer.AddSpacer(5)

        # Email Password

        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordLabel = wx.StaticText(panel, -1, "Password",
                                   size=(195, -1), style=wx.ALIGN_RIGHT)
        passwordSizer.Add(passwordLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        passwordSizer.AddSpacer(5)

        passwordText = wx.TextCtrl(panel, -1, "", size=(200, -1),
                                   style=wx.TE_PASSWORD)
        passwordSizer.Add(passwordText, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.Add(passwordSizer, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        sizer.AddSpacer(20)

        # Line

        line = wx.StaticLine(panel, -1, size=(100, -1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.RIGHT)

        sizer.AddSpacer(20)

        # Lock

        lockSizer = wx.BoxSizer(wx.HORIZONTAL)
        lockLabel = wx.StaticText(panel, -1, "Lock",
                                   size=(195, -1), style=wx.ALIGN_RIGHT)
        lockSizer.Add(lockLabel, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        lockSizer.AddSpacer(5)
        lockText = wx.TextCtrl(panel, -1, "", size=(200, -1),
                                   style=wx.TE_PASSWORD)
        lockSizer.Add(lockText, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sizer.Add(lockSizer, 0, wx.ALIGN_CENTER_VERTICAL, 5)

        panel.SetSizer(sizer)



if __name__ == '__main__':
    app = wx.App()
    frm = SigninFrame(None)
    frm.Show()
    app.MainLoop()