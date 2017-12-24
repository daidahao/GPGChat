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
## Class Frame1
###########################################################################

class Frame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add", pos = wx.DefaultPosition, size = wx.Size( 373,233 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4.SetMinSize( wx.Size( 400,400 ) ) 
		fgSizer1 = wx.FlexGridSizer( 3, 0, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.addtip1 = wx.StaticText( self, wx.ID_ANY, u"Please enter the name you want to add", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.addtip1.Wrap( -1 )
		self.addtip1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer21.Add( self.addtip1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer1.Add( bSizer21, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.addname1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer131.Add( self.addname1, 0, wx.ALIGN_CENTER|wx.ALL|wx.TOP, 10 )
		
		
		bSizer111.Add( bSizer131, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer111, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.addconfirm1 = wx.Button( self, wx.ID_ANY, u"confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.addconfirm1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer4.Add( fgSizer1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

