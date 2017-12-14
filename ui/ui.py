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

class SigninFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SignIn", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = 0|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"night2_resize.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 300,500 ), 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL, 0 )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetFont( wx.Font( 8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Sign up", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "微软雅黑" ) )
		
		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( bSizer4 )
		self.m_panel3.Layout()
		bSizer4.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 20 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SignupFrame
###########################################################################

class SignupFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GPGChat", pos = wx.DefaultPosition, size = wx.Size( 500,323 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		frameSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		panelSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.signupLabel = wx.StaticText( self.panel, wx.ID_ANY, u"SIGNUP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.signupLabel.Wrap( -1 )
		self.signupLabel.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		panelSizer.Add( self.signupLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		subSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		subsubSizer = wx.BoxSizer( wx.VERTICAL )
		
		emailSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.emailLabel = wx.StaticText( self.panel, wx.ID_ANY, u"E-mail", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_RIGHT )
		self.emailLabel.Wrap( -1 )
		emailSizer.Add( self.emailLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.emptyLabel1 = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 4,-1 ), 0 )
		self.emptyLabel1.Wrap( -1 )
		emailSizer.Add( self.emptyLabel1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.emailText = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		emailSizer.Add( self.emailText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		subsubSizer.Add( emailSizer, 1, wx.EXPAND, 5 )
		
		passwordSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.passwordLabel = wx.StaticText( self.panel, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_RIGHT )
		self.passwordLabel.Wrap( -1 )
		passwordSizer.Add( self.passwordLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.emptyLabel2 = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 4,-1 ), 0 )
		self.emptyLabel2.Wrap( -1 )
		passwordSizer.Add( self.emptyLabel2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.emailSizer = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		passwordSizer.Add( self.emailSizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		subsubSizer.Add( passwordSizer, 1, wx.EXPAND, 5 )
		
		smtpSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.smtpLabel = wx.StaticText( self.panel, wx.ID_ANY, u"SMTP Server", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_RIGHT )
		self.smtpLabel.Wrap( -1 )
		smtpSizer.Add( self.smtpLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.emptyLabel3 = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 4,-1 ), 0 )
		self.emptyLabel3.Wrap( -1 )
		smtpSizer.Add( self.emptyLabel3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.smtpText = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		smtpSizer.Add( self.smtpText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		subsubSizer.Add( smtpSizer, 1, wx.EXPAND, 5 )
		
		nameSIzer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.nameLabel = wx.StaticText( self.panel, wx.ID_ANY, u"Your Real Name", wx.DefaultPosition, wx.Size( 110,-1 ), wx.ALIGN_RIGHT )
		self.nameLabel.Wrap( -1 )
		nameSIzer.Add( self.nameLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.emptyLabel4 = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 4,-1 ), 0 )
		self.emptyLabel4.Wrap( -1 )
		nameSIzer.Add( self.emptyLabel4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nameText = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		nameSIzer.Add( self.nameText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		subsubSizer.Add( nameSIzer, 1, wx.EXPAND, 5 )
		
		bottomSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		signupButtonSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.signupButton = wx.Button( self.panel, wx.ID_ANY, u"Signup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.signupButton.SetDefault() 
		signupButtonSizer.Add( self.signupButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		bottomSizer.Add( signupButtonSizer, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.space = wx.StaticText( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 10,-1 ), 0 )
		self.space.Wrap( -1 )
		bottomSizer.Add( self.space, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		quitButtonSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.quitButton = wx.Button( self.panel, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		quitButtonSizer.Add( self.quitButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		bottomSizer.Add( quitButtonSizer, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		subsubSizer.Add( bottomSizer, 1, wx.BOTTOM|wx.EXPAND, 10 )
		
		
		subSizer.Add( subsubSizer, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 40 )
		
		
		panelSizer.Add( subSizer, 1, wx.EXPAND, 5 )
		
		
		self.panel.SetSizer( panelSizer )
		self.panel.Layout()
		panelSizer.Fit( self.panel )
		frameSizer.Add( self.panel, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 20 )
		
		
		self.SetSizer( frameSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.signupButton.Bind( wx.EVT_BUTTON, self.OnSignup )
		self.quitButton.Bind( wx.EVT_BUTTON, self.OnQuit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSignup( self, event ):
		event.Skip()
	
	def OnQuit( self, event ):
		event.Skip()
	

###########################################################################
## Class LockDialog
###########################################################################

class LockDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"LOCK", pos = wx.DefaultPosition, size = wx.Size( 261,131 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		subSizer = wx.BoxSizer( wx.VERTICAL )
		
		subsubSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.lockLabel = wx.StaticText( self, wx.ID_ANY, u"Please enter your lock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockLabel.Wrap( -1 )
		subsubSizer.Add( self.lockLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		subsubSizer.Add( self.lockText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockButton = wx.Button( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockButton.SetDefault() 
		subsubSizer.Add( self.lockButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		subSizer.Add( subsubSizer, 1, wx.EXPAND, 5 )
		
		
		sizer.Add( subSizer, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 20 )
		
		
		self.SetSizer( sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lockButton.Bind( wx.EVT_BUTTON, self.OnLockButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnLockButton( self, event ):
		event.Skip()
	

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GPGChat", pos = wx.DefaultPosition, size = wx.Size( 693,401 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel13 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetMaxSize( wx.Size( 100,-1 ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button13 = wx.Button( self.m_panel13, wx.ID_ANY, u"联系人", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button14 = wx.Button( self.m_panel13, wx.ID_ANY, u"最近聊天", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button15 = wx.Button( self.m_panel13, wx.ID_ANY, u"黑名单", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( bSizer31 )
		self.m_panel13.Layout()
		bSizer25.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.list = wx.ListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
		bSizer34.Add( self.list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel14.SetSizer( bSizer34 )
		self.m_panel14.Layout()
		bSizer25.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
		bSizer25.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer25 )
		self.m_panel6.Layout()
		bSizer25.Fit( self.m_panel6 )
		sizer.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

