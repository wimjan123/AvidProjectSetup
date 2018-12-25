import wx

app = wx.App()

frmf = wx.Frame(None, title="NLE_KeyConvert")

def avid_button_clicked(event):


avid_button = wx.Button(frmf, label="Avid Media Composer", size=(0.4,3))
avid_button.Bind(wx.EVT_BUTTON, avid_button_clicked)


frmf.Show()



app.MainLoop()
