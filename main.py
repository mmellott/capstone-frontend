# -*- coding: utf-8 -*-
import Tkinter as tk

def add_scrollbar(widget):
	scrollbar = tk.Scrollbar(widget)
	scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	scrollbar.config(command=widget.yview)


class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)

		## create a menu
		# top level
		menubar = tk.Menu(self.master)

		# file menu
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open Workbook")
		filemenu.add_command(label="Save Workbook")
		filemenu.add_command(label="New Workbook")
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.master.quit)

		# edit menu
		editmenu = tk.Menu(menubar, tearoff=0)
		editmenu.add_command(label="Cut")
		editmenu.add_command(label="Copy")
		editmenu.add_command(label="Paste")

		# help menu
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About")

		# add menus to toplevel and display
		menubar.add_cascade(label="File", menu=filemenu)
		menubar.add_cascade(label="Edit", menu=editmenu)
		menubar.add_cascade(label="Help", menu=helpmenu)
		self.master.config(menu=menubar)

		## editor group 
		# widgets
		editor_group = tk.LabelFrame(self, text="Editor")

		sbars = []
		for i in range(2):
			sbars.append(tk.Scrollbar(editor_group))

		self.lesson_text = tk.Text(editor_group, bg="#FFFFD9", yscrollcommand=sbars[0].set)
		self.lesson_text.insert(tk.END, "Lesson text.")
		self.lesson_text.config(state=tk.DISABLED)
		self.editor = tk.Text(editor_group, yscrollcommand=sbars[1].set)
		button_frame = tk.Frame(editor_group)

		self.run_button = tk.Button(button_frame, text="Run")
		self.run_button.config(bg='green')
		self.stop_button = tk.Button(button_frame, text="Stop")
		self.stop_button.config(bg='red')

		sbars[0].config(command=self.lesson_text.yview)
		sbars[1].config(command=self.editor.yview)

		# layout
		for i in range(2):
			editor_group.grid_rowconfigure(i, weight=1)
		editor_group.grid_columnconfigure(0, weight=1)
		self.lesson_text.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=5, pady=5)
		self.editor.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W, padx=5, pady=(0,5))
		h = editor_group.winfo_height()
		self.lesson_text.config(height=h/10)
		button_frame.grid(row=2, column=0, sticky=tk.E+tk.W+tk.S)
		self.run_button.pack(fill=tk.X, expand=1, pady=(0,2), padx=5)
		self.stop_button.pack(fill=tk.X, expand=1, pady=(0,5),padx=5)
		sbars[0].grid(row=0, column=1, sticky=tk.N+tk.S, padx=(0,5), pady=5)
		sbars[1].grid(row=1, column=1, sticky=tk.N+tk.S, padx=(0,5), pady=(0,5))

		## lesson group 
		lesson_group = tk.LabelFrame(self, text="Lessons", padx=5, pady=5)

		self.lesson_listbox = tk.Listbox(lesson_group)
		self.lesson_listbox.insert(tk.END, "Sandbox Mode") # at index 0
		for i in range(1, 6): # 5 lessons
			self.lesson_listbox.insert(tk.END, "Lesson " + str(i))
		self.lesson_listbox.select_set(1) # start with lesson 1 selected

		self.selectButton = tk.Button(lesson_group, text='Select Lesson', command=self.select_lesson, bg='skyblue')

		## layout
		# main frame layout 
		self.pack(fill=tk.BOTH, expand=1)

		# layout of widgets in main frame
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		lesson_group.grid(row=0, column=0, sticky=tk.N + tk.S, padx=10, pady=(5,10))
		editor_group.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W, padx=(0,10), pady=(5,10))

		# layout of widgets in lesson group
		lesson_group.grid_rowconfigure(0, weight=1)
		lesson_group.grid_columnconfigure(0, weight=1)
		self.lesson_listbox.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.selectButton.grid(row=1, column=0, sticky=tk.S, pady=5)


	def select_lesson(self):
		#self.test_v.set(self.lesson_listbox.curselection())
		pass


app = Application()
app.master.title('Prototype')
app.master.geometry(("%dx%d")%(809,500))
app.mainloop()

