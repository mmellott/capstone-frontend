#!/usr/bin/python
""" Define Lesson class that holds lesson data to be used by the interface.
Lesson text is loaded from html files in lessons/. Main program will just
call get_lessons to get a list of all lessons that the interface should
present. """

import os
import ConfigParser

class LessonManager:
    """ Basically just a struct of lesson related data. """

    def __init__(self):

        self.lessons = ConfigParser.ConfigParser()
        self.lessons.read('lessons.ini')

    def GetInstructions(self, lid):
        return self.lessons.get("Lesson"+str(lid), "instructions")

    def ShowMain(self, lid):
        return self.lessons.getboolean("Lesson"+str(lid), "main")

    def ShowLoop(self, lid):
        return self.lessons.getboolean("Lesson"+str(lid), "loop")

if __name__ == '__main__':
    pass # test _lesson.py
