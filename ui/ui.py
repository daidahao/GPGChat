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
		
		self.passwordText = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		passwordSizer.Add( self.passwordText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GPGChat", pos = wx.DefaultPosition, size = wx.Size( 832,401 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel13 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetMaxSize( wx.Size( 100,-1 ) )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.contactButton = wx.Button( self.m_panel13, wx.ID_ANY, u"Contact", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.contactButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.recentButton = wx.Button( self.m_panel13, wx.ID_ANY, u"Most Recent", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.recentButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.blacklistButton = wx.Button( self.m_panel13, wx.ID_ANY, u"Blacklist", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer31.Add( self.blacklistButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( bSizer31 )
		self.m_panel13.Layout()
		bSizer25.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.list = wx.ListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.LC_REPORT|wx.SUNKEN_BORDER )
		bSizer37.Add( self.list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer34.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		self.addContactButton = wx.Button( self.m_panel14, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.addContactButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		
		bSizer36.Add( bSizer38, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.removeContactButton = wx.Button( self.m_panel14, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.removeContactButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer36.Add( bSizer39, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.blockContactButton = wx.Button( self.m_panel14, wx.ID_ANY, u"Block", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.blockContactButton, 0, wx.ALL, 5 )
		
		
		bSizer36.Add( bSizer40, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer34.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		
		self.m_panel14.SetSizer( bSizer34 )
		self.m_panel14.Layout()
		bSizer25.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel15 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TAB_TRAVERSAL )
		flexSizer = wx.FlexGridSizer( 2, 0, 0, 0 )
		flexSizer.SetFlexibleDirection( wx.BOTH )
		flexSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		flexSizer.SetMinSize( wx.Size( -1,250 ) ) 
		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_scrolledWindow1.SetMinSize( wx.Size( -1,220 ) )
		self.m_scrolledWindow1.SetMaxSize( wx.Size( -1,220 ) )
		
		wrapSizer = wx.WrapSizer( wx.VERTICAL )
		
		wrapSizer.SetMinSize( wx.Size( -1,220 ) ) 
		self.emptyText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.emptyText.Wrap( -1 )
		wrapSizer.Add( self.emptyText, 0, wx.ALL, 5 )
		
		self.sendText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Ha ha ha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sendText.Wrap( 250 )
		self.sendText.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.sendText.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )
		self.sendText.Hide()
		
		wrapSizer.Add( self.sendText, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.recvText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.recvText.Wrap( 250 )
		self.recvText.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.recvText.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )
		self.recvText.Hide()
		
		wrapSizer.Add( self.recvText, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( wrapSizer )
		self.m_scrolledWindow1.Layout()
		wrapSizer.Fit( self.m_scrolledWindow1 )
		flexSizer.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.inputText = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,100 ), wx.TE_MULTILINE )
		bSizer42.Add( self.inputText, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		self.sendButton = wx.Button( self.m_panel15, wx.ID_ANY, u"SEND", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer42.Add( self.sendButton, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer49.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		
		flexSizer.Add( bSizer49, 1, wx.EXPAND, 5 )
		
		
		self.m_panel15.SetSizer( flexSizer )
		self.m_panel15.Layout()
		bSizer25.Add( self.m_panel15, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer25 )
		self.m_panel6.Layout()
		bSizer25.Fit( self.m_panel6 )
		sizer.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.contactButton.Bind( wx.EVT_BUTTON, self.OnContactButton )
		self.recentButton.Bind( wx.EVT_BUTTON, self.OnRecentButton )
		self.blacklistButton.Bind( wx.EVT_BUTTON, self.OnBlacklistButton )
		self.addContactButton.Bind( wx.EVT_BUTTON, self.OnAddContactButton )
		self.removeContactButton.Bind( wx.EVT_BUTTON, self.OnRemoveContactButton )
		self.blockContactButton.Bind( wx.EVT_BUTTON, self.OnBlockContactButton )
		self.sendButton.Bind( wx.EVT_BUTTON, self.OnSend )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnContactButton( self, event ):
		event.Skip()
	
	def OnRecentButton( self, event ):
		event.Skip()
	
	def OnBlacklistButton( self, event ):
		event.Skip()
	
	def OnAddContactButton( self, event ):
		event.Skip()
	
	def OnRemoveContactButton( self, event ):
		event.Skip()
	
	def OnBlockContactButton( self, event ):
		event.Skip()
	
	def OnSend( self, event ):
		event.Skip()
	

###########################################################################
## Class LockFrame
###########################################################################

class LockFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 273,139 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		subSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.lockLabel = wx.StaticText( self, wx.ID_ANY, u"Please enter your lock", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockLabel.Wrap( -1 )
		subSizer.Add( self.lockLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		subSizer.Add( self.lockText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockButton = wx.Button( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockButton.SetDefault() 
		subSizer.Add( self.lockButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sizer.Add( subSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		
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
## Class AddContactFrame
###########################################################################

class AddContactFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Contact", pos = wx.DefaultPosition, size = wx.Size( 273,139 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		sizer = wx.BoxSizer( wx.VERTICAL )
		
		subSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.lockLabel = wx.StaticText( self, wx.ID_ANY, u"Please enter the email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockLabel.Wrap( -1 )
		subSizer.Add( self.lockLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		subSizer.Add( self.lockText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lockButton = wx.Button( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lockButton.SetDefault() 
		subSizer.Add( self.lockButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sizer.Add( subSizer, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lockButton.Bind( wx.EVT_BUTTON, self.OnConfirmButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnConfirmButton( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseContactFrame
###########################################################################

class ChooseContactFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Contact", pos = wx.DefaultPosition, size = wx.Size( 481,298 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		self.label = wx.StaticText( self, wx.ID_ANY, u"Please choose the user you want to add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label.Wrap( -1 )
		bSizer37.Add( self.label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		self.m_listCtrl3 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
		bSizer37.Add( self.m_listCtrl3, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.confirmButton = wx.Button( self, wx.ID_ANY, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.confirmButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer38.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.cancelButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer38.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		
		bSizer37.Add( bSizer38, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer34.Add( bSizer37, 1, wx.EXPAND, 10 )
		
		
		self.SetSizer( bSizer34 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.confirmButton.Bind( wx.EVT_BUTTON, self.OnConfirmButton )
		self.cancelButton.Bind( wx.EVT_BUTTON, self.OnCancelButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnConfirmButton( self, event ):
		event.Skip()
	
	def OnCancelButton( self, event ):
		event.Skip()
	

