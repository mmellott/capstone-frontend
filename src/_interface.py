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
import wx,os
import wx.html2
import _lesson

# Create a new frame class, derived from the wxPython Frame.
class MyFrame(wx.Frame):
    """ This is the main frame of the app and will display lessons. """

    def __init__(self, parent, ident, title, app, lessons):
        """ The constructor... """
        # First, call the base class' __init__ method to create the frame
        wx.Frame.__init__(self, parent, ident, title)
        self.app = app # app.load needs to be called to load program
        self.Centre()
        self.SetSize((900, 700))
        self.lessons = lessons
        self.currentLesson = self.lessons[0]

        self.header = self.HackStyle(ReadFile('html/header.html'))
        self.footer = self.HackStyle(ReadFile('html/footer.html'))
        
        # Load the first lesson
        self.html = wx.html2.WebView.New(self)

        self.SetLessonPage()
        
        self.Bind(wx.html2.EVT_WEBVIEW_NAVIGATING, self.onLinkClicked, self.html)

    # When the html is being navigated
    def onLinkClicked(self, event):
        
        # when a new lesson is selected
        if(event.GetURL().find("lesson") >= 0):
            lesson_num = int(str(event.GetURL()).split("-")[1])
            self.currentLesson = self.lessons[lesson_num]
            self.SetLessonPage()

        # When code is uploaded
        elif(len(event.GetURL()) > 0):
            event.Veto()
            self.app.load(event.GetURL(), event.GetURL()) 
            """data = self.GetFieldData(self.html.GetPageSource())
            if(len(data) > 0): main = data[data.keys()[0]]
            else: main = ""
            if(len(data) > 1): loop = data[data.keys()[1]]
            else: loop = ""
            self.app.load(main, loop) 
            event.Veto()"""

        # Prevent looping
        if(event.GetURL() != None):
            event.Veto()

    # Build the html page with the header body and footer
    def SetLessonPage(self):
        page = str(self.header) + self.currentLesson.GetPageSource() + str(self.footer)
        self.html.SetPage(page, "")
        

    # Hack to retreive the submitted form data
    def GetFieldData(self, source):
        data = {}
        split = source.split('<textarea')
        postload = (len(split) == 1)
        if(postload): split = source.split('<TEXTAREA')
        for field in split[1:]:
            if(postload):
                key = field.split('id=')
                if(len(key)>1): key = (field.split('id=')[1]).split(' ')[0]
                else: key = "field-" + str(split.index(field)-1)
                data[key] = ((field.split('>')[1]).split('</TEXTAREA>')[0][:-10])
            else:
                key = field.split('id="')
                if(len(key)>1): key = (field.split('id="')[1]).split('"')[0]
                else: key = "field-" + str(split.index(field)-1)
                data[key] = ((field.split('>')[1]).split('</textarea>')[0][:-10])
        print data
        return data

    def HackStyle(self, source):

        style = source.split("<link ")
        for element in style:
            if(element.find(">") < element.find('href="') or element.find('href="') == -1):
                continue
            part = element.split(">")[0]
            src = (part.split('href="')[1]).split('"')[0]

            source = source[:source.find(part)-6]+'<style type="text/css">'+str(ReadFile("html"+src))+'</style>'+source[source.find(part)+len(part)+1:]

        style = source.split('<script ')
        for element in style:
            if(element.find(">") < element.find('src="') or element.find('src="') == -1):
                continue
            part = element.split(">")[0]
            src = (part.split('src="')[1]).split('"')[0]

            source = source[:source.find(part)-8]+'<script type="text/javascript">'+str(ReadFile("html"+src))+'</script>'+source[source.find(part)+len(part)+1:]
            
        return source

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

