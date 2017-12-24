from ui.ui import SignupFrame, MainFrame, LockFrame, AddContactFrame, ChooseContactFrame
import wx
import time
from wx.lib.mixins.listctrl import ColumnSorterMixin


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
            print("Initializing LockFrame")

        if (type == LockDialogType.NOLOCK):
            self.lockLabel.SetLabelText("Please set your lock first")
            self.lockButton.SetLabelText("Set")

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
                    if (self.setlock()):
                        dlg = wx.MessageDialog(self,
                                               "Your lock is set successfully!",
                                               "Success", wx.OK)
                        dlg.ShowModal()
                        # dlg.Destroy()
                        #
                        # frame = self.__class__(None, LockDialogType.HASLOCK,
                        #                      self.lock, self.verbose)
                        # frame.Show()
                        self.starthaslockframe()

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

                    frame = self.__class__(None)
                    frame.Show()

                    self.Close()
        else:
            self.lock = self.lockText.GetValue()
            if (self.islockcorrect()):
                frame = MainFrameMod(None)
                frame.Show()
                self.Close()
            else:
                dlg = wx.MessageDialog(self,
                                       "Your lock is incorrect!",
                                       "Failure", wx.OK)
                dlg.ShowModal()
                self.lockText.SetValue("")
                self.lock = ""

    def setlock(self):
        pass

    def islockcorrect(self):
        pass

    def checklock(self):
        if self.lock is None or self.lock == "":
            dlg = wx.MessageDialog(self,
                                   "Your lock cannot be empty!",
                                   "Warning", wx.OK)
            dlg.ShowModal()
            return False
        return True

    def starthaslockframe(self):
        pass


contact_data = {
    1: ("Dai", "daidahao@icloud.com", "9999999", time.time()),
    2: ("Zou", "999@test.com", "9999999", time.time() - 3600),
    3: ("Sun", "test@test.com", "9999999", time.time() + 36000),
}

blacklist_data = {
    1: ("China Mobile", "123@10086.com", "9999999", 0),
    2: ("China Telcom", "123@10000.com", "9999999", 0)
}

def time_to_string(t):
    t_localtime = time.localtime(t)
    localtime = time.localtime()
    if (t_localtime.tm_year == localtime.tm_year
        and t_localtime.tm_mon == localtime.tm_mon
        and t_localtime.tm_mday == localtime.tm_mday):
        return time.strftime("%H:%M:%S", t_localtime)
    return time.strftime("%Y-%m-%d %H:%M:%S", t_localtime)


class MainFrameMod(MainFrame, ColumnSorterMixin):
    def GetListCtrl(self):
        return self.list

    def __init__(self, parent):
        MainFrame.__init__(self, parent)
        self.count = 0
        self.allText = []
        self.itemDataMap = {}
        self.OnContactButton(None)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        self.currentItem = -1
        self.blacklistDisplayed = False

    def PopulateList(self, data1):
        self.itemDataMap = data1
        self.currentItem = -1

        self.list.ClearAll()
        ColumnSorterMixin.__init__(self, 4)
        # for normal, simple columns, you can add them like this:
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

    def OnContactButton( self, event ):
        self.PopulateList(contact_data)
        self.SortListItems(0, 1)
        self.blacklistDisplayed = False

    def OnRecentButton( self, event ):
        self.PopulateList(contact_data)
        self.SortListItems(3, 1)
        self.blacklistDisplayed = False

    def OnBlacklistButton( self, event ):
        self.PopulateList(blacklist_data)
        self.SortListItems(0, 1)
        self.blacklistDisplayed = True

    def ShowWarningMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                               'Warning',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def CheckIfItemSelected(self):
        if (-1 == self.currentItem):
            dlg = wx.MessageDialog(self, 'You havn\'t selected any item!',
                                   'Warning',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def ShowYesNoMessage(self, message):
        dlg = wx.MessageDialog(self, message,
                               'Warning',
                               wx.YES_NO | wx.ICON_INFORMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return result

    def GetCurrentNameText(self):
        return self.list.GetItem(self.currentItem, 0).GetText()

    def OnAddContactButton( self, event ):
        # The function of adding to the blacklist by hand
        # could be considered in a later version
        if (self.blacklistDisplayed):
            self.ShowWarningMessage('You cannot add to the blacklist for now.')
            return
        addContactFrame = AddContactFrameMod(self)
        addContactFrame.Show()

    def OnRemoveContactButton( self, event ):
        if (self.blacklistDisplayed):
            return
        self.CheckIfItemSelected()

        name = self.GetCurrentNameText()
        result = self.ShowYesNoMessage(
            'Are you sure to remove %s from the list?' % (name))

        if result == wx.ID_YES:
            print("Removing %s..." % name)
        else:
            print("The user cancel the removing operation.")

    def OnBlockContactButton( self, event ):
        if (self.blacklistDisplayed):
            self.CheckIfItemSelected()
            return
        self.CheckIfItemSelected()

        name = self.GetCurrentNameText()
        result = self.ShowYesNoMessage('Are you sure to block %s?' % (name))

        if result == wx.ID_YES:
            print("Blocking %s..." % name)
        else:
            print("The user cancel the removing operation.")

    def OnItemSelected(self, event):
        self.currentItem = event.Index
        name = self.list.GetItem(self.currentItem, 0).GetText()
        # print(self.list.GetItem(self.currentItem, 2).GetText())

class AddContactFrameMod(AddContactFrame):
    def __init__(self, parent):
        AddContactFrame.__init__(self, parent)
        self.parent = parent

    def OnConfirmButton( self, event ):
        chooseContactFrame = ChooseContactFrameMod(self.parent)
        chooseContactFrame.Show()
        self.Close()


class ChooseContactFrameMod(ChooseContactFrame):
    def OnConfirmButton( self, event ):
        self.Close()

    def OnCancelButton( self, event ):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    # dialog = LockDialogMod(None)
    # dialog.Show()
    frame = LockFrameMod(None, verbose=True)
    frame.Show()
    app.MainLoop()
