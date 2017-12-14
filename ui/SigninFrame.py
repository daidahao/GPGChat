# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class SigninFrame
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class SigninFrame
###########################################################################

class SigninFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"SignIn", pos=wx.DefaultPosition, size=wx.Size(700, 500),
                          style=0 | wx.NO_BORDER | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, -1), wx.Size(-1, -1))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_bitmap1 = wx.StaticBitmap(self, wx.ID_ANY,
                                         wx.Bitmap(u"night2_resize.jpg",
                                                   wx.BITMAP_TYPE_ANY), wx.DefaultPosition, wx.Size(300, 500), 0)
        bSizer1.Add(self.m_bitmap1, 0, wx.ALL, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    frm = SigninFrame(None)
    frm.Show()
    app.MainLoop()