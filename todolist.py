# created 18 June 2022
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()
root.title('MY TO DO LIST')
root.geometry('570x500+2000+200')

pale_blue = '#caede5'
red = '#e83a54'

class Menu_Bar:	
	def __init__(self):
		# create menu bar
		self.my_menu = Menu(root)
		root.config(menu=self.my_menu)

		# labeling menu bar
		self.file_menu = Menu(self.my_menu, tearoff=0)
		self.my_menu.add_cascade(label='File', menu=self.file_menu)

		# add item in menu bar
		self.file_menu.add_command(label='Save List', command=self.save_list)
		self.file_menu.add_command(label='Open List', command=self.open_list)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit', command=lambda:root.quit())

	def save_list(self):
		# gather item in listbox
		stuff = box.listbox.get(0, END)

		# define path to save file
		filetype = [('Text', '*.txt')]
		savefile_path = filedialog.asksaveasfilename(title='Save File',filetype=filetype, defaultextension=filetype)

		#save file
		with open(savefile_path, 'r', newline='') as f:
			for line in stuff:
				f.write(line + '\n')

	def open_list(self):
		filetype = [('Text', '*.txt')]
		openfile_path = filedialog.askopenfilename(title='Open File', filetype=filetype, defaultextension=filetype)

		# delete the old item in listbox first when user click to open file
		if openfile_path:
			box.listbox.delete(0, END)
			with open(openfile_path, 'r') as f:
				for line in f:
					box.listbox.insert(END, line)
		

class Box:
	def __init__(self):
		self.frame = Frame(root)
		self.frame.pack()

		self.listbox = Listbox(self.frame, font=my_font(20), width=34, height=8, bd=0, activestyle='none', bg=pale_blue)
		self.listbox.pack(side=LEFT, fill=BOTH)

	def list_stuff(self):
		stuff = ['This', 'is', 'a', 'dummy', 'list']
		# stuff = []
		for i in stuff:
			self.listbox.insert(END, i)

		my_scrollbar = Scrollbar(self.frame)
		my_scrollbar.pack(side=RIGHT, fill=BOTH)

		self.listbox.config(yscrollcommand=my_scrollbar.set)
		my_scrollbar.config(command=self.listbox.yview)


class User_Entry:
	def __init__(self):
		self.frame = Frame(root)
		self.frame.pack()

		self.list_label = Label(self.frame, text='Add: ', font=my_font(13))
		self.list_label.grid(row=0, column=1, pady=20)

		self.entry = Entry(self.frame, font=my_font(15))
		self.entry.grid(row=0, column=2, pady=20)


class Btn:
	def __init__(self):
		self.frame = Frame(root)
		self.frame.pack()

		self.add_btn = Button(self.frame, text='ADD To List',font=my_font(10), command=self.add)
		self.add_btn.grid(row=0, column=0, pady=10, padx=10)

		self.delete_btn = Button(self.frame, text='Delete',font=my_font(10), command=self.delete)
		self.delete_btn.grid(row=0, column=1, padx=10)

		self.cross_btn = Button(self.frame, text='Grey Out Item',font=my_font(10), command=self.cross)
		self.cross_btn.grid(row=0, column=2, padx=10)

		self.uncross_btn = Button(self.frame, text='Ungrey Item',font=my_font(10), command=self.uncross)
		self.uncross_btn.grid(row=0, column=3, padx=10)

		self.delete_cross_btn = Button(self.frame, text='Delete Grey Item', font=my_font(10), command=self.delete_cross)
		self.delete_cross_btn.grid(row=0, column=4, padx=10)

		self.delete_all_btn = Button(self.frame, text='Delete ALL', font=my_font(10), fg=red, command=self.delete_all)
		self.delete_all_btn.grid(row=1, column=2, pady=10)

	def add(self):
		box.listbox.insert(END, entry.entry.get())
		entry.entry.delete(0, END)

	def delete(self):
		box.listbox.delete(ANCHOR)

	def cross(self):
		box.listbox.itemconfig(box.listbox.curselection(), fg='grey')
		box.listbox.selection_clear(0, END)

	def uncross(self):
		box.listbox.itemconfig(box.listbox.curselection(), fg='black')
		box.listbox.selection_clear(0, END)

	def delete_cross(self):
		count = 0
		while count < box.listbox.size():
			if box.listbox.itemcget(count, 'fg') == 'grey':
				box.listbox.delete(box.listbox.index(count))
			else:
				count += 1

	def delete_all(self):
		box.listbox.delete(0, END)


def my_font(num):
	my_font = Font(family='Comic Sans MS', weight='bold', size=num)
	return my_font

menu_bar = Menu_Bar()

box = Box()
box.list_stuff()

entry = User_Entry()
btn = Btn()

root.bind('<Escape>', lambda x:root.quit())
root.mainloop()
