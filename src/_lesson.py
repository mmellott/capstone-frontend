#!/usr/bin/python
""" Define Lesson class that holds lesson data to be used by the interface.
Lesson text is loaded from html files in lessons/. Main program will just
call get_lessons to get a list of all lessons that the interface should
present. """

import os
import _interface

class Lesson:
    """ Basically just a struct of lesson related data. """

    def __init__(self, number):
        """ The setup_and_loop flag lets the interface know wether setup and
        loop text boxes should be shown. Notice that in lesson one there is
        only one text box presented to the user and it is implicitly a loop
        box. Setup is introduce later. The text is just the lesson text. """

        self.lesson_id = number

        # read saved data from a file and store here
        self.saved_data = []

        # load the template for the page
        self.page = _interface.ReadFile("lessons/lesson"+str(self.lesson_id)+".html")
        
    def GetPageSource(self):
        # insert saved data here.

        page = self.page.replace('{SAVE}','')
        
        return page

        

def get_lessons(lesson_dir):
    """ Add lessons to lessons and return. """
    lessons = {}
    
    for index in range(0, 9):
        lessons[index] = (Lesson(index))

    return lessons

if __name__ == '__main__':
    pass # test _lesson.py

