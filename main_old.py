#!/usr/bin/python
""" This is the main program file. """
from src import _lesson
from src import _interface
from src import _loader
from src import _finddev
from src import _error
import wx

class MyApp(wx.App):
    """ Main application. """

    def load(self, setup, loop):
        """ Use _loader module to load program onto Arduino via serial. """
        if not(_finddev.exists(self.dev)):
            self.dev = _finddev.finddev()
        if self.dev == "":
            return _error.Error(_error.ARDUINO_NOT_FOUND)
        prg = _loader.makeprg(setup, loop)

        # _loader.load might return something other than None in future
        error = _loader.load(self.dev, self.baud, prg)
        return error

    def OnInit(self):
        """ Initialize application config and then interface config. """
        # we don't like to overide __init__ for wx.App so vars defined here
        self.dev = _finddev.finddev()
        self.baud = 57600
        self.lesson_dir = "lessons/"

        frame = _interface.MyFrame(None,
                                   -1,
                                   "WINDOW TITLE",
                                   self,
                                   _lesson.get_lessons(self.lesson_dir))
        frame.Show(True)
        self.SetTopWindow(frame)
        return True # return success flag


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()

