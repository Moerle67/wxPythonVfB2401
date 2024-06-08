import Windows1, wx

class WorkWindows1(Windows1.MyWindow1):
    def OnBtnSaveClicked( self, event ):
        print("Button gedrückt")
        event.Skip()



class MainApp(wx.App):
    def OnInit(self):
       self.fenster1 = WorkWindows1(None)
       self.fenster1.Show(True) 
       return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()