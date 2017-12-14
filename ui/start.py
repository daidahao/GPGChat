#!/bin/python
"""
Hello World, but with more meat.
"""

import wx

class SigninFrame(wx.Frame):
    """
    A Frame that says Hello World
    """

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(SigninFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        fgs = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        pnl.SetSizer(fgs)

        email_text_static = wx.StaticText(pnl, -1, label="E-mail",
                                          size=(120, -1),
                                          style=wx.ALIGN_RIGHT)
        font = email_text_static.GetFont()
        font.PointSize += 5
        font = font.Bold()
        email_text_static.SetFont(font)
        fgs.Add(email_text_static)

        email_text_ctrl = wx.TextCtrl(pnl, -1, size=(180, -1));
        fgs.Add(email_text_ctrl)

        password_text_static = wx.StaticText(pnl, label="Password", pos=(40, 50),
                                             size=(120, -1),
                                             style=wx.ALIGN_RIGHT)
        password_text_static.SetFont(font)
        fgs.Add(password_text_static)

        password_text_ctrl = wx.TextCtrl(pnl, size=(180, -1), style=wx.TE_PASSWORD)
        fgs.Add(password_text_ctrl)


        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to GPGChat!")


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = SigninFrame(None, title='Signin')
    frm.Show()
    app.MainLoop()