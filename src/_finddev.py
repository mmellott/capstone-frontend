#!/usr/bin/python
""" The finddev function must be able to find the Arduino regardless of what
file it is assigned to in /dev. In Ubuntu, this has always been /dev/ttyACM0,
but it will probably be different on the Pi. And this could also be different
depending on the number of devices plugged into the Pi or the order they are
plugged in.  Implementing this functionality might be difficult. I have not been
able to find many great examples. Worst case scenario we could hardcode it and
wait till it breaks to fix it... """
import os.path

def exists(dev):
    """ Check to see if dev still exists. """
    return (os.path.isfile(dev) and os.path.exists(dev))

def finddev():
    """ Find the Arduino. """
    # some pseudo code:
    #     find dev
    #     if dev_plugged_in:
    #         return dev
    #     else:
    #         return ""
    return '/dev/ttyACM0'

