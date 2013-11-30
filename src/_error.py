#!/usr/bin/python
""" Objects of type Error are returned if there was an error loading bitlash
code onto the Arduino. If you would like to add a new error add an entry in the
error code table and add a handler in the __str__ method. """

################################################################################
# error codes
#
ARDUINO_NOT_FOUND = 1
SYNTAX = 2


################################################################################
# Error class
#
class Error:
    """ Signifies a load error. """

    def __init__(self, error_code):
        """ Construct an Error with just an error_code from list above. """
        self.error_code = error_code

    def __str__(self):
        """ Cast obj of type Error to str (like if we want to print it). """ 
        if self.error_code == ARDUINO_NOT_FOUND:
            return 'The Arduino cannot be found. Make sure it is plugged in.' 
        elif self.error_code == SYNTAX:
            return 'There was a syntax error in your program.'
        else:
            return 'Unknown error.'

