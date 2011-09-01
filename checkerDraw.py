import random
import wx
import time

class MyPanel(wx.Panel):
    """ class MyPanel creates a panel to draw on, inherits wx.Panel """
    def __init__(self, parent, id):
        # create a panel
        wx.Panel.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def OnPaint(self, evt):
        self.dc = wx.PaintDC(self)
        self.dc.Clear()
        self.dc.BeginDrawing()
        self.dc.SetPen(wx.Pen("BLACK",1))
        r =  g =  b = 256 ##set black squares
        for row in range(0,8):
            if row%2 == 0:
                for col in range(8):
                    if col%2 != 0:
                        self.dc.SetBrush(wx.Brush((r, g, b), wx.SOLID))
                        w = 50
                        h = w
                        x = w*row
                        y = w*col
                        self.dc.DrawRectangle(x, y, w, h)
                        time.sleep(0.2)  # delay for dramatic effect
            else:
                for col in range(8):
                    if col%2 == 0:
                        self.dc.SetBrush(wx.Brush((r, g, b), wx.SOLID))
                        w = 50
                        h = w
                        x = w*row
                        y = w*col
                        self.dc.DrawRectangle(x, y, w, h)
                        time.sleep(0.2)  # delay for dramatic effect
        self.dc.EndDrawing()
        # free up the device context now
        del self.dc
        
        
height1 = 435
width1 = 415

app = wx.PySimpleApp()
# create a window/frame, no parent, -1 is default ID
frame = wx.Frame(None, -1, "Drawing Checkerboard", size = (width1, height1))
# call the derived class, -1 is default ID
MyPanel(frame,-1)
# show the frame
frame.Show(True)
# start the event loop
app.MainLoop()
