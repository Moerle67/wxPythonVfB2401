import Windows1, wx

class MainApp(wx.App):
    def OnInit(self):
       self.fenster1 = Windows1.MyWindow1(None)
       self.fenster1.Show(True) 
       return True
    
if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()