#!/usr/bin/python
""" Functions in here handle loading bitlash programs onto the Arduino. """
# import _error # might need this if we actually caught exceptions?
import serial, fdpexpect, time

def waitprompt(c):
    """ Wait until we see a prompt. """
    c.expect('\n> ')
    time.sleep(0.1)

def makeprg(setup, loop):
    """ We can only handle one line prgs with no setup right now... """
    return ('while 1 { %stwinkle(); }\n' % (loop))

def load(device, baud, program):
    """ Load a bitlash program onto the Arduino. """
    serialport = serial.Serial(device, baud, timeout=0)
    c = fdpexpect.fdspawn(serialport.fd)
    #c.logfile_read = sys.stdout
    # synch with the command prompt
    c.sendline('')
    waitprompt(c)
    # do stuff
    if(program.find('\n')>=0):
        #program is many lines
        text = program.split('\n')
        for line in text:
            line = line.strip()
            print(line)
            if (len(line) > 0) and (line[0] != '#'):
                c.sendline(line)
                waitprompt(c)
                print("waiting for prompt after twinkle")
    else:
        #program is one line
        if (len(program) > 0) and (line[0] != '#'):
            c.sendline(program)
            waitprompt(c)
    c.close()
    print("Done")
    return None

if __name__ == "__main__":
    #prog = ["pixel(0, 0, green); draw_all()\n"]
    prog = ["while 1 {twinkle();}\n"]
    load('/dev/ttyACM0', 57600, prog)

