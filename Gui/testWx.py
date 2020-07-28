import wx

app = wx.App()
frame = wx.Frame( None, wx.ID_ANY, "Hello világ" )
frame.SetBackgroundColour( wx.BLUE )
panel01 = wx.Panel( frame, wx.ID_ANY )
panel01.SetBackgroundColour( wx.YELLOW )
panel02 = wx.Panel( panel01, wx.ID_ANY, pos = ( 20,20 ), size = ( 200,100 ))
panel02.SetBackgroundColour( wx.RED )
button = wx.Button( panel02, wx.ID_ANY, "Gomb", pos = ( 80, 20 ), size = ( 80, 20 ))
frame.Show( True )
app.MainLoop()