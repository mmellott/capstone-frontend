#!/usr/bin/python
""" The MyFrame class below is pretty much taken from the link below with a few
changes related to our project:

    http://www.wxpython.org/test7.py.html

The wx module supports html windows via the wx.html.HtmlWindow class. This
should allows us to support an interface that looks pretty similar to what we
had before. We might even be able to reuse some of their markup. It might help
to checkout this example:

    http://wiki.wxpython.org/wxPython%20by%20Example

You will probably need to remove a lot of the code below. The current
functionality is just for the sake of example. """
import wx

# Create a new frame class, derived from the wxPython Frame.
class MyFrame(wx.Frame):
    """ This is the main frame of the app and will display lessons. """

    def __init__(self, parent, ident, title, app, lessons):
        """ The constructor... """
        # First, call the base class' __init__ method to create the frame
        wx.Frame.__init__(self, parent, ident, title)
        self.app = app # app.load needs to be called to load program
        self.lessons = lessons

        # Associate some events with methods of this class
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MOVE, self.OnMove)

        # Add a panel and some controls to display the size and position
        panel = wx.Panel(self, -1)
        label1 = wx.StaticText(panel, -1, "Size:")
        label2 = wx.StaticText(panel, -1, "Pos:")
        self.sizeCtrl = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY)
        self.posCtrl = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY)
        self.panel = panel

        # Use some sizers for layout of the widgets
        sizer = wx.FlexGridSizer(2, 2, 5, 5)
        sizer.Add(label1)
        sizer.Add(self.sizeCtrl)
        sizer.Add(label2)
        sizer.Add(self.posCtrl)

        border = wx.BoxSizer()
        border.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizerAndFit(border)
        self.Fit()


    # This method is called by the System when the window is resized,
    # because of the association above.
    def OnSize(self, event):
        """ Just for example. """
        size = event.GetSize()
        self.sizeCtrl.SetValue("%s, %s" % (size.width, size.height))

        # tell the event system to continue looking for an event handler,
        # so the default handler will get called.
        event.Skip()

    # This method is called by the System when the window is moved,
    # because of the association above.
    def OnMove(self, event):
        """ Just for example. """
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


if __name__ == '__main__':
    pass # test MyFrame

