#!/usr/bin/python
""" Define Lesson class that holds lesson data to be used by the interface.
Lesson text is loaded from html files in lessons/. Main program will just
call get_lessons to get a list of all lessons that the interface should
present. """

class Lesson:
    """ Basically just a struct of lesson related data. """

    def __init__(self, setup_and_loop, text):
        """ The setup_and_loop flag lets the interface know wether setup and
        loop text boxes should be shown. Notice that in lesson one there is
        only one text box presented to the user and it is implicitly a loop
        box. Setup is introduce later. The text is just the lesson text. """
        self.setup_and_loop = setup_and_loop
        self.text = text
        # any other data needed?
 

def _get_text(fname):
    """ Get lesson text from file with name fname in lesson_dir`. """
    pass

def get_lessons(lesson_dir):
    """ Add lessons to lessons and return. """
    lessons = []
    lessons.append(Lesson(False,
                          _get_text(lesson_dir + 'lesson1.html'))) # lesson 01
    # lesson 02
    # lesson 03
    # lesson 04
    # lesson 05
    # lesson 06
    # lesson 08
    # lesson 09
    # lesson 10
    return lessons

if __name__ == '__main__':
    pass # test _lesson.py

