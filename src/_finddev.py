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
    #library for calling shell commands 
    import subprocess
    #first find the bus number and port number that Arduino resides on
    proc = subprocess.Popen("dmesg | grep Arduino", stdout = subprocess.PIPE, shell = True)
    line = proc.stdout.readline()
    if line != '':
        string = line.rstrip()
        print "bus & port:", string
    else:
        print("ERROR: unable to find device file in file system.")
        return ""
    #extract bus_port number
    pos_start = string.find("usb ")
    pos_end = string.find(":")
    bus_port = string[pos_start+4:pos_end]
    #print(bus_port)
    #search for the dev file information in kernel logs 
    #dev will be either ttyUSB* or ttyACM*
    cmd = 'dmesg | grep "' + bus_port + '"' + '| grep "tty"'
    #print(cmd) 
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
    line = proc.stdout.readline()
    if line != '':
        string = line.rstrip()
        print ":", string
    else:
        print("ERROR: unable to find device file in file system.")
        return "dev file:"
    pos_start = string.find("tty")
    pos_end = string.find(":",pos_start)
    dev = string[pos_start:pos_end] 
    dev = "/dev/" + dev
    #print("testout:",dev) 
    return dev

