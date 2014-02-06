#!/usr/bin/python
""" This is the main program file. """
from src import _lesson
from src import _interface
from src import _loader
from src import _finddev
from src import _error
from Tkinter import Tk

class MyApp(Tk):
    """ Main application. """

    def load(self, loop):
        """ Use _loader module to load program onto Arduino via serial. """
        if not(_finddev.exists(self.dev)):
            self.dev = _finddev.finddev()
        if self.dev == "":
            return _error.Error(_error.ARDUINO_NOT_FOUND)
        prg = _loader.makeprg("", loop)

        # _loader.load might return something other than None in future
        error = _loader.load(self.dev, self.baud, prg)
        return error

    def __init__(self, parent):
        """ Initialize application config and then interface config. """
        # we don't like to overide __init__ for wx.App so vars defined here

        Tk.__init__(self)  
        self.dev = _finddev.finddev()
        self.baud = 57600
        
        self.lessons = _lesson.LessonManager()
        
        frame = _interface.MyFrame(self, parent)
        
        return None # return success flag


if __name__ == '__main__':
    app = MyApp(None)
    app.title('Program Lessons')
    app.geometry("700x600+10+10")
    app.mainloop()

