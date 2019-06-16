#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
from pages import *


class window():

	def __init__(self):
		self.root = Tk()
		self.root.title("NOME DO PROGRAMA? tem q ver dps") # "GUI - these Rammouz"
		#self.root.geometry('800x600')
		#self.root.configure(background="black")
		self.text_font = tkfont.Font(family='Verdana', size=13)#, weight="bold", slant="italic")
		
		self.flag=1
	


		corner_frame_top = Frame(width=40, height=20, bg="", colormap="new")
		corner_frame_top.grid(column=0, row=0)
		self.central_frame = Frame(width=500, height=500, bg="", colormap="new")
		self.central_frame.grid(column=1, row=1)
		corner_frame_bottom = Frame(width=40, height=20, bg="", colormap="new")
		corner_frame_bottom.grid(column=3, row=3)

		self.init_pages()

		self.show_frame("StartPage")
		
		self.next_button = Button(self.root, text = "Next", command=self.next_page)
		self.next_button.grid(column=7, row=7, sticky=E)
		
		self.root.mainloop()

	def next_page(self):

		# test
		if(self.flag==1):
			self.show_frame("TestPage")
			self.flag = 2
		elif(self.flag==2):
			self.show_frame("EndPage")
			self.flag = 1
			self.next_button.config(text="Done", command=self.quit)

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()

	def init_capteurs_pages(self, numCapteurs):
		# TODO
		pass
		#for i in range(numCapteurs):

	def init_pages(self):
		self.frames = {}
		#frame_names = ["StartPage", "ComposantsPage", "ProblemePage", "EndPage"]

		# start page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["StartPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")
		# put all of the pages in the same location;
		# the one on the top of the stacking order
		# will be the one that is visible.

		# start page
		start_text = "Start page"
		self.start_lbl = Label(self.frames["StartPage"] , text=start_text, font=self.text_font)
		self.start_lbl.pack()

		# test page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["TestPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# test page
		test_text = "testy"
		self.test_lbl = Label(self.frames["TestPage"] , text=test_text, font=self.text_font)
		self.test_lbl.pack()

		# end page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["EndPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# end page
		end_text = "end page xD"
		self.end_lbl = Label(self.frames["EndPage"] , text=end_text, font=self.text_font)
		self.end_lbl.pack()




	def quit(self):
		self.root.destroy()