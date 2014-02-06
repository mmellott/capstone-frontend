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
from Tkinter import *
from ttk import Frame, Button, Label, Style
import tkFont, os
import _lesson
import math

# Create a new frame class, derived from the wxPython Frame.
class MyFrame(Frame):
    """ This is the main frame of the app and will display lessons. """

    def __init__(self, app, parent):
        Frame.__init__(self, parent)
        self.app = app

        self.keyWords = ['for', 'in', 'while', 'do', 'if', 'break', 'continue', 'return']
        self.functions = ['twinkle']
        
        self.initUI()
        
        self.ChangeLesson(1)
        
    def initUI(self):
        self.style = Style()
        #self.style.theme_use("clam")
        self.pack(fill=BOTH, expand=1)

        background_image=PhotoImage("IMG_1060.JPG")
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

        helv36 = tkFont.Font(family="Arial",size=24,weight="bold")
        helv12 = tkFont.Font(family="Arial",size=12)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #self.columnconfigure(1, minsize=200)
        #self.rowconfigure(3, weight=1)
        #self.rowconfigure(5, pad=7)

        
        lbl = Label(self, text="Program Lessons", font=helv36)
        lbl.config(background="white")
        lbl.grid(sticky=W, pady=4, padx=5, columnspan=3)


        nav = Frame(self)
        content = Frame(self, borderwidth=0)
        #content.grid_propagate(False)
        
        nav.grid(row=1, column=0, padx=2, sticky=N)
        content.grid(row=1, column=1, padx=4, sticky=N+W+E+S)

        content.columnconfigure(0, weight=1)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        
        self.instructions = Text(content, fg="#000000", bg="#FFFFFF", bd=0, relief="flat", height=0, wrap=WORD, font=helv12)
        self.instructions.grid(row=0, column=0, sticky=N+E+W, columnspan=2)
        self.instructions.config(state=DISABLED)
        
        #create the main text are with scrollbars
        xscrollbar = Scrollbar(content, orient=HORIZONTAL)
        xscrollbar.grid(row=2, column=0, sticky=E + W)

        yscrollbar = Scrollbar(content, orient=VERTICAL)
        yscrollbar.grid(row=1, column=1, sticky=N + S)

        self.textarea = Text(content, wrap=NONE, tabs="0.4i", bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        self.textarea.bind('<<Modified>>', self.TextEntered)
        #self.textarea.bind_class("post-class-bindings", "<Key>", self.TextEntered)
        self.textarea.grid(row=1, column=0, padx=0, sticky=E+W+S+N)

        xscrollbar.config(command=self.textarea.xview)
        yscrollbar.config(command=self.textarea.yview)

        btn = Button(content, text="Run", command=self.ExecuteProgram)
        btn.grid(row=3, column=0, pady=2, padx=2, sticky=E+S)

        for i in range(1, 11):
            btn = Button(nav, text="Lesson " + str(i), command=lambda i=i:self.ChangeLesson(i))
            btn.grid(row=i, column=0, pady=2)

        self.textarea.tag_config("error", background="#FF7777")
        self.textarea.tag_config("keyword", foreground="#FF7700")
        self.textarea.tag_config("normal", foreground="#000000")
        self.textarea.tag_config("string", foreground="#00AA00")
        self.textarea.tag_config("number", foreground="#00FFFF")
        self.textarea.tag_config("function", foreground="#0000FF")
        
    def ChangeLesson(self, number):
        self.instructions.config(state=NORMAL)
        self.instructions.delete("1.0",END)
        self.instructions.insert(END, self.app.lessons.GetInstructions(number))
        self.instructions.config(height=self.instructions.index("end-1c").split(".")[0])
        print self.instructions.index("end-1c")
        self.instructions.config(height=int(math.ceil(float(self.instructions.index("end-1c").split('.')[1]) / float(self.instructions['width']))))
        #self.instructions.config(state=DISABLED)
        

    def ExecuteProgram(self):
        print "EXECUTING"
        self.app.load(self.textarea.get("0.0", END))

    def TextEntered(self, x):
        number = self.textarea.index(INSERT).split(".")[0]
        line = self.textarea.get(number+".0", END).split("\n")[0]
        length = len(line)

        pos = 0
        letters = self.GenerateColorCodeList(line)
        for letter in letters:
            for tag in self.textarea.tag_names(number+"."+str(pos)):
                self.textarea.tag_remove(tag, number+"."+str(pos))
            self.textarea.tag_add(letter, number+"."+str(pos))
            pos += 1


        self.textarea.edit_modified(False)


    def GenerateColorCodeList(self, string):
        marks = []
        for letter in string:
            marks.append("normal")

        # Find Strings
        on = 0
        pos = 0
        for letter in string:
            if letter == '"' or letter == "'":
                on = (on+1) % 2
                marks[pos] = "string"
            if on == 1:
                marks[pos] = "string"
            pos += 1

        # Find keywords and functions
        marks = self.MarkKeyWords(marks, string, "keyword", self.keyWords)
        marks = self.MarkKeyWords(marks, string, "function", self.functions)
        return marks
        
    def MarkKeyWords(self, marks, string, mark, words):
        for word in words:
            pos = 0
            while(pos < len(string)):
                nxt = string.find(word, pos)
                
                # The word was not found
                if nxt == -1: break
                pos = nxt + len(word)

                # the word was found. check to be sure its not part of another word
                if nxt > 0 and string[nxt-1].isalnum(): continue
                if pos < len(string) and string[pos].isalnum(): continue

                for letter in word:
                    if(marks[nxt] != "normal"): break
                    marks[nxt] = mark
                    nxt += 1
        return marks


# Read data from a file
def ReadFile(filepath):
    try:
        with open(filepath) as f:
            content = f.readlines()
        return '\r\n'.join(content)
    except:
        return False
    
if __name__ == '__main__':
    pass # test MyFrame

