from ui.ui import SignupFrame, MainFrame, LockFrame, AddContactFrame, ChooseContactFrame
import wx
import time
from wx.lib.mixins.listctrl import ColumnSorterMixin

#注册窗口
class SignupFrameMod(SignupFrame):
    def OnSignup(self, event):
        if self.check_signup():
            self.showsuccess()
            self.start_lock_frame()
        else:
            pass
#取消注册
    def OnQuit(self, event):
        self.Destroy()
#显示已成功注册的窗口
    def showsuccess(self):
        dlg = wx.MessageDialog(self,
                               "Signup successfully!",
                               "Success",
                               wx.OK)
        dlg.Center()
        dlg.ShowModal()
        dlg.Destroy()
#显示注册失败窗口
    def showfailure(self, message="Cannot signup!"):
        dlg = wx.MessageDialog(self,
                               message,
                               "Failure",
                               wx.OK)
        dlg.Center()
        dlg.ShowModal()
        dlg.Destroy()
#确认是否输入邮箱，若否，弹出窗口
    def checkmail(self):
        self.mail = self.emailText.GetValue()
        if self.mail == "":
            self.showfailure("Email cannot be empty")
            return False
        return True
#确认是否输入密码，若否，弹出该窗口
    def checkpassword(self):
        self.password = self.passwordText.GetValue()
        if self.password == "":
            self.showfailure("Password cannot be empty")
            return False
        return True

#确认是否输入SMTP Server。若否，弹出窗口
    def checkserver(self):
        self.server = self.smtpText.GetValue()
        if self.server == "":
            self.showfailure("SMTP Server cannot be empty")
            return False
        return True
#确认是否输入名字，若否，弹出窗口
    def checkname(self):
        self.name = self.nameText.GetValue()
        if self.name == "":
            self.showfailure("Name cannot be empty")
            return False
        return True

    def checkimapserver(self):
        self.imapserver = self.imapText.GetValue()
        if self.imapserver == "":
            self.showfailure("IMAP Server cannnot be empty")
            return False
        return True

#确认注册完成
    def check_signup(self):
        if (self.checkmail() and
                self.checkpassword() and
                self.checkserver() and
                self.checkname() and
                self.checkimapserver()):
            return True
        return False
#打开lock界面
    def start_lock_frame(self):
        pass




class LockDialogType:
    NOLOCK, HASLOCK = range(2)
#lock相关的窗口操作
class LockFrameMod(LockFrame):
    #设置lock
    def __init__(self, parent,
                 type=LockDialogType.NOLOCK, lock=None, verbose=False):

        LockFrame.__init__(self, parent)
        self.type = type
        self.lock = lock
        self.verbose = verbose

        if self.verbose:
            print("Initializing LockFrame")

        if (type == LockDialogType.NOLOCK):
            self.lockLabel.SetLabelText("Please set your lock first")
            self.lockButton.SetLabelText("Set")
#确认lock是否能正常使用的一系列操纵与提示窗口
    def OnLockButton(self, event):
        if (self.type == LockDialogType.NOLOCK):
            if (self.lock == None):
                self.lock = self.lockText.GetValue()
                self.lockText.SetValue("")
                # print(self.checklock())
                if self.lock is None or self.lock == "":
                    dlg = wx.MessageDialog(self,
                                           "Your lock cannot be empty!",
                                           "Warning", wx.OK)
                    dlg.ShowModal()
                    self.lock = None
                else:
                    self.lockLabel.SetLabelText("Please confirm your lock")
                    self.lockButton.SetLabelText("Confirm")
            else:
                if (self.lock == self.lockText.GetValue()):
                    if (self.set_lock()):
                        dlg = wx.MessageDialog(self,
                                               "Your lock is set successfully!",
                                               "Success", wx.OK)
                        dlg.ShowModal()
                        # dlg.Destroy()
                        #
                        # frame = self.__class__(None, LockDialogType.HASLOCK,
                        #                      self.lock, self.verbose)
                        # frame.Show()
                        self.start_has_lock_frame()

                        self.Close()
                    else:
                        dlg = wx.MessageDialog(self,
                                               "Cannot set up the lock!",
                                               "Failure", wx.OK)
                        dlg.ShowModal()
                        self.Close()
                else:
                    dlg = wx.MessageDialog(self,
                                           "The confirmed lock is inconsistent with the "
                                           "previous one. Please try again!",
                                           "Failure", wx.OK)
                    dlg.ShowModal()
                    # dlg.Destroy()

                    # frame = self.__class__(None)
                    # frame.Show()
                    self.start_no_lock_frame()

                    self.Close()
        else:
            self.lock = self.lockText.GetValue()
            if (self.is_lock_correct()):
                self.strat_main_frame()
                self.Close()
            else:
                dlg = wx.MessageDialog(self,
                                       "Your lock is incorrect!",
                                       "Failure", wx.OK)
                dlg.ShowModal()
                self.lockText.SetValue("")
                self.lock = ""
#不存在lock的窗口
    def start_no_lock_frame(self):
        frame = self.__class__(None, None, self.verbose)
        frame.Show()

    def set_lock(self):
        pass

    def is_lock_correct(self):
        pass
##确认是否输入lock，若否，弹出提示窗口
    def check_lock(self):
        if self.lock is None or self.lock == "":
            dlg = wx.MessageDialog(self,
                                   "Your lock cannot be empty!",
                                   "Warning", wx.OK)
            dlg.ShowModal()
            return False
        return True

    def start_has_lock_frame(self):
        pass
#打开主聊天窗口
    def strat_main_frame(self):
        frame = MainFrameMod(None)
        frame.Show()

#从电脑获取当前年月日
def time_to_string(t):
    t_localtime = time.localtime(t)
    localtime = time.localtime()
    if (t_localtime.tm_year == localtime.tm_year
        and t_localtime.tm_mon == localtime.tm_mon
        and t_localtime.tm_mday == localtime.tm_mday):
        return time.strftime("%H:%M:%S", t_localtime)
    return time.strftime("%Y-%m-%d %H:%M:%S", t_localtime)

#登录成功后聊天主界面，包括联系人，黑名单，最近聊天人，聊天窗口
class MainFrameMod(MainFrame, ColumnSorterMixin):



    def GetListCtrl(self):
        return self.list

    def __init__(self, parent):
        MainFrame.__init__(self, parent)

        # 初始化联系人数据
        self.contact_data = {}
        # 初始黑名单数据
        self.blacklist_data = {}

        self.contactCanBeRead = False
        self.count = 0
        self.allText = []
        self.itemDataMap = {}
        self.OnContactButton(None)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        self.currentItem = -1
        self.blacklistDisplayed = False
        self.staticTextList = []


    #联系人列表及相关信息
    def PopulateList(self, data1):
        self.itemDataMap = data1
        self.currentItem = -1

        self.list.ClearAll()
        ColumnSorterMixin.__init__(self, 4)
        self.list.InsertColumn(0, "Name")
        self.list.InsertColumn(1, "Email")
        self.list.InsertColumn(2, "KeyID")
        self.list.InsertColumn(3, "Last Message")
        items = data1.items()
        for key, data in items:
            index = self.list.InsertItem(self.list.GetItemCount(), data[0])
            # print(index)
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2 ,data[2])
            self.list.SetItem(index, 3, time_to_string(data[3]))
            self.list.SetItemData(index, key)

        self.list.SetColumnWidth(0, 50)
        self.list.SetColumnWidth(1, 100)
        self.list.SetColumnWidth(2, 100)
        self.list.SetColumnWidth(3, 150)
#从窗口获取需要发送信息并发送
    def OnSend( self, event ):
        self.AddSendMessage(self.inputText.GetValue())

    def AddSendMessage(self, message):
        self.AddMessage(send=True, message=message)
#获取接收到的信息并显示在窗口中
    def AddRecvMessage(self, message):
        self.AddMessage(send=False, message=message)

    def AddMessage(self, send=True, message=""):
        wrapSizer = self.m_scrolledWindow1.GetSizer()
        self.count = self.count + 1

        textCtrl = wx.StaticText(self.m_scrolledWindow1, wx.ID_HIGHEST + 1, message, wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        # textCtrl.SetLabelText(message)
        textCtrl.Wrap(250)
        textCtrl.SetForegroundColour(wx.Colour(255, 255, 255))
        textCtrl.SetBackgroundColour(wx.Colour(0, 128, 255))
        # textCtrl.SetMaxSize(wx.Size(200, -1))

        if (send):
            wrapSizer.Add(textCtrl, 0, wx.ALL | wx.ALIGN_RIGHT, 5)
        else:
            wrapSizer.Add(textCtrl, 0, wx.ALL | wx.ALIGN_LEFT, 5)

        self.staticTextList.append(textCtrl)


        self.m_scrolledWindow1.SetSizerAndFit(wrapSizer)
        wrapSizer.Layout()
        self.m_scrolledWindow1.Layout()
        self.m_panel15.Layout()

        self.m_scrolledWindow1.Scroll(0, self.m_scrolledWindow1.GetScrollRange(wx.VERTICAL))

    # 清空窗口显示的发送接收信息
    def ClearAllMessages(self):
        for staticText in self.staticTextList:
            # wrapSizer = self.m_scrolledWindow1.GetSizer()
            # wrapSizer.Remove(staticText)
            staticText.Destroy()
        self.count = 0
        self.staticTextList.clear()

    #选择联系人
    def OnContactButton( self, event ):
        self.blockContactButton.SetLabelText("Block")
        self.ReadContactData()
        self.PopulateList(self.contact_data)
        self.SortListItems(0, 1)
        self.blacklistDisplayed = False
        self.EnableInput()

    def OnRecentButton( self, event ):
        self.blockContactButton.SetLabelText("Block")
        self.ReadContactData()
        self.PopulateList(self.contact_data)
        self.SortListItems(3, 0)
        self.blacklistDisplayed = False
        self.EnableInput()

    # 选择黑名单
    def OnBlacklistButton( self, event ):
        self.blockContactButton.SetLabelText("Unblock")
        self.ReadBlacklistData()
        self.PopulateList(self.blacklist_data)
        self.SortListItems(0, 1)
        self.blacklistDisplayed = True
        self.DisableInput()

    # 提示信息
    def ShowWarningMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                               'Warning',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    # 提示信息
    def ShowSuccessMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                               'Success',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    # 确认是否正确选择
    def CheckIfItemSelected(self):
        if (-1 == self.currentItem):
            dlg = wx.MessageDialog(self, 'You havn\'t selected any item!',
                                   'Warning',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return False
        return True
    # 确认信息是否正确输入窗口
    def ShowYesNoMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                               'Warning',
                               wx.YES_NO | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return result
#获取当前联系人名字
    def GetCurrentNameText(self):
        return self.list.GetItem(self.currentItem, 0).GetText()
#添加联系人窗口
    def OnAddContactButton( self, event ):
        # The function of adding to the blacklist by hand
        # could be considered in a later version
        self.ClearAllMessages()
        if (self.blacklistDisplayed):
            self.ShowWarningMessage('You cannot add to the blacklist for now.')
            return
        self.StartAddContactFrame()

    # 删除联系人窗口
    def OnRemoveContactButton( self, event ):
        # if (self.blacklistDisplayed):
        #     return
        self.ClearAllMessages()
        if not self.CheckIfItemSelected():
            return

        name = self.GetCurrentNameText()
        result = self.ShowYesNoMessage(
            'Are you sure to remove %s from the list?' % (name))

        if result == wx.ID_YES:
            print("Removing %s..." % name)
            if not self.remove_contact(self.GetCurrentKeyId()):
                self.ShowWarningMessage("Cannot remove the contact")
                return
            if self.blacklistDisplayed:
                self.OnBlacklistButton(None)
            else:
                self.OnContactButton(None)
        else:
            print("The user cancel the removing operation.")

    # 获取黑名单联系人
    def OnBlockContactButton( self, event ):
        # if self.blacklistDisplayed:
        #     return
        self.ClearAllMessages()
        if not self.CheckIfItemSelected():
            return

        name = self.GetCurrentNameText()
        result = self.ShowYesNoMessage('Are you sure to block/unblock %s?' % (name))

        if result == wx.ID_YES:
            print("Blocking %s..." % name)
            if not self.block_contact(self.GetCurrentKeyId()):
                self.ShowWarningMessage("Cannot block/unblock the contact")
                return
            if self.blacklistDisplayed:
                self.OnBlacklistButton(None)
            else:
                self.OnContactButton(None)
        else:
            print("The user cancel the removing operation.")
#选择操作
    def OnItemSelected(self, event):
        self.currentItem = event.Index
        name = self.list.GetItem(self.currentItem, 0).GetText()
        # print(self.list.GetItem(self.currentItem, 2).GetText())

    def DisableInput(self):
        self.inputText.Disable()
        self.sendButton.Disable()

    def EnableInput(self):
        self.inputText.Enable()
        self.sendButton.Enable()

    def StartAddContactFrame(self):
        addContactFrame = AddContactFrameMod(self)
        addContactFrame.Show()

    def ReadContactData(self):
        pass

    def remove_contact(self, keyid):
        return True

    def GetCurrentKeyId(self):
        if self.currentItem == -1:
            return None
        return self.list.GetItem(self.currentItem, 2).GetText()

    def ReadBlacklistData(self):
        pass

    def block_contact(self, param):
        return True




#添加联系人窗口设计
class AddContactFrameMod(AddContactFrame):
    def __init__(self, parent):
        AddContactFrame.__init__(self, parent)
        self.parent = parent
        self.email = None
        self.keysmap = {}

    #添加button
    def OnConfirmButton( self, event ):
        if not self.check_email():
            return
        if not self.check_gpg():
            return
        self.StartChooseContactFrame()
        self.Close()

    # 提示信息
    def ShowWarningMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                                'Warning',
                                 wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def check_email(self):
        self.email = self.emailText.GetValue()
        if self.email == "":
            self.ShowWarningMessage("Email cannot be empty!")
            return False
        return True

    def StartChooseContactFrame(self):
        chooseContactFrame = ChooseContactFrameMod(self.parent, self.keysmap)
        chooseContactFrame.Show()

    def check_gpg(self):
        return True


# 选择联系人窗口设计
class ChooseContactFrameMod(ChooseContactFrame, ColumnSorterMixin):

    def GetListCtrl(self):
        return self.list

    def __init__(self, parent, keysmap):
        ChooseContactFrame.__init__(self, parent)
        self.parent = parent
        self.itemDataMap = {}
        self.currentItem = -1
        self.PopulateList(keysmap)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)

    # 确认button
    def OnConfirmButton( self, event ):
        if self.currentItem == -1:
            self.ShowWarningMessage("You haven't selected any item yet!")
            self.Close()

    # 取消button
    def OnCancelButton( self, event ):
        self.Close()

    def PopulateList(self, data1):
        self.itemDataMap = self.keysmap_to_datamap(data1)
        self.currentItem = -1

        self.list.ClearAll()
        ColumnSorterMixin.__init__(self, 3)
        self.list.InsertColumn(0, "Name")
        self.list.InsertColumn(1, "Email")
        self.list.InsertColumn(2, "Key ID")
        items = data1.items()
        for key, data in items:
            index = self.list.InsertItem(self.list.GetItemCount(), data['name'])
            self.list.SetItem(index, 1, data['mail'])
            self.list.SetItem(index, 2, data['keyid'])

        self.list.SetColumnWidth(0, 100)
        self.list.SetColumnWidth(1, 100)
        self.list.SetColumnWidth(2, 200)

    def keysmap_to_datamap(self, keysmap):
        result = {}
        for key, data in keysmap.items():
            result[key] = (data['name'], data['mail'], data['keyid'])
        return result

    def OnItemSelected(self, event):
        self.currentItem = event.Index

    # 提示信息
    def ShowWarningMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                                'Warning',
                                wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    # dialog = LockDialogMod(None)
    # dialog.Show()
    frame = LockFrameMod(None, verbose=True)
    frame.Show()
    app.MainLoop()
