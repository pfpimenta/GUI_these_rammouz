#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
from convenience import *
from Add_new_capteur_window import *


DEFAULT_NUM_CAP = 1 # capteurs
DEFAULT_NUM_ADC = 1 # ADCs
DEFAULT_NUM_MSP = 1 # microprocesseurs
DEFAULT_NUM_MEM = 1 # memoires
DEFAULT_NUM_RF = 1 # modules radiofrequence


START_PAGE_TEXT = "start page aeaeae\n\naqui vo deixar uma descricao\nblablablabla\n\nGUI coded by Pedro FOLETTO PIMENTA"
END_PAGE_TEXT =  "Press \"Done\" to start simulation"


# global variable with the simulation parameters 
params = {}
params['numCapteurs'] = 0
params['numADCs'] = 0
params['numMicroprocesseurs'] = 0
params['numMemoires'] = 0
params['numModulesRadiofrequence'] = 0



class window():

	def __init__(self):
		
		self.flag=1 # temporary
		
		# windows general layout
		self.init_main_layout()

		# init pages (start, composants, probleme, end)
		self.init_pages()

		# begin by start page
		self.show_frame("StartPage")
		
		# run mainloop
		self.root.mainloop()

	def init_main_layout(self):
		### init window:
		self.root = Tk()
		self.root.title("NOME DO PROGRAMA? tem q ver dps") # "GUI - these Rammouz"
		#self.root.geometry('800x600')
		#self.root.configure(background="black")
		### set text font:
		self.text_font = tkfont.Font(family='Verdana', size=13)#, weight="bold", slant="italic")
		### central frame (where the pages are placed)
		self.central_frame = Frame(self.root, width=500, height=500)#, bg="", colormap="new")
		self.central_frame.grid(column=2, row=2)
		### Next/Done button
		self.next_button = Button(self.root, text = "Next", command=self.next_page)
		self.next_button.grid(column=4, row=4, sticky=E)
		### Back button (previous page)
		self.back_button = Button(self.root, text = "Back", command=self.previous_page)
		self.back_button.grid(column=1, row=4, sticky=E)
		### padding
		pad_frame_top_1 = Frame(self.root,width=50, height=30)#, bg="", colormap="new")
		pad_frame_top_1.grid(column=0, row=0)
		pad_frame_top_2 = Frame(self.root, width=50, height=30)#, bg="", colormap="new")
		pad_frame_top_2.grid(column=1, row=1)
		pad_frame_mid = Frame(self.root, width=50, height=30)#, bg="", colormap="new")
		pad_frame_mid.grid(column=3, row=3)
		pad_frame_bottom = Frame(self.root, width=30, height=25)#, bg="", colormap="new")
		pad_frame_bottom.grid(column=10, row=10)

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()
		self.current_page = page_name
		self.update_buttons()
		
	def update_buttons(self):
		# no back button in start page
		if(self.current_page=="StartPage"):
			self.back_button.grid_forget()
		else:
			self.back_button.grid(column=1, row=4, sticky=E)

		# next button becomes Done button in end page
		if(self.current_page=="EndPage"):
			self.next_button.config(text="Done", command=self.quit)
		else:
			self.next_button.config(text="Next", command=self.next_page)
		
	def init_probleme_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["ProblemePage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Add new capteur \n #TODO"
		self.test_lbl = Label(self.frames["ProblemePage"] , text=text, font=self.text_font)
		self.test_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.frames["ProblemePage"], height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.frames["ProblemePage"])
		frame_for_entries.grid(row=2, column=0)

		self.add_capteur_button = Button(self.frames["ProblemePage"], text = "Add new capteur", command=self.add_new_capteur)
		self.add_capteur_button.grid(column=1, row=1, sticky=E)

	def init_composants_page(self):

		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["NumComposantsPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# text
		text = "Saisissez le nombre de chaque composant, svp"
		self.composants_lbl = Label(self.frames["NumComposantsPage"] , text=text, font=self.text_font)
		self.composants_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.frames["NumComposantsPage"], height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.frames["NumComposantsPage"])
		frame_for_entries.grid(row=2, column=0)

		### NUM CAPTEURS
		lbl_numCapteurs = Label(frame_for_entries, text="num. de Capteurs:")
		lbl_numCapteurs.grid(column=1, row=1)

		s_numCapteurs = StringVar()
		self.entry_numCapteurs = Entry(frame_for_entries, textvariable=s_numCapteurs)
		self.entry_numCapteurs.grid(column=2, row=1)
		s_numCapteurs.set(str(DEFAULT_NUM_CAP))

		### NUM ADCs
		lbl_numADCs = Label(frame_for_entries, text="num. de ADCs:")
		lbl_numADCs.grid(column=1, row=2)

		s_numADCs = StringVar()
		self.entry_numADCs = Entry(frame_for_entries, textvariable=s_numADCs)
		self.entry_numADCs.grid(column=2, row=2)
		s_numADCs.set(str(DEFAULT_NUM_ADC))

		### NUM microprocesseurs
		lbl_numMSPs = Label(frame_for_entries, text="num. de microprocesseurs:")
		lbl_numMSPs.grid(column=1, row=3)

		s_numMSPs = StringVar()
		self.entry_numMSPs = Entry(frame_for_entries, textvariable=s_numMSPs)
		self.entry_numMSPs.grid(column=2, row=3)
		s_numMSPs.set(str(DEFAULT_NUM_MSP))

		### NUM memoires
		lbl_numADCs = Label(frame_for_entries, text="num. de memoires:")
		lbl_numADCs.grid(column=1, row=4)

		s_numMems = StringVar()
		self.entry_numMems = Entry(frame_for_entries, textvariable=s_numMems)
		self.entry_numMems.grid(column=2, row=4)
		s_numMems.set(str(DEFAULT_NUM_MEM))

		### NUM modules radiofrequence
		lbl_numRFs = Label(frame_for_entries, text="num. de modules radiofrequence:")
		lbl_numRFs.grid(column=1, row=5)

		s_numRFs = StringVar()
		self.entry_numRFs = Entry(frame_for_entries, textvariable=s_numRFs)
		self.entry_numRFs.grid(column=2, row=5)
		s_numRFs.set(str(DEFAULT_NUM_RF))

	def init_start_page(self):

		# create page
		frame = Frame(self.central_frame)
		self.frames["StartPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# text
		self.start_lbl = Label(self.frames["StartPage"] , text=START_PAGE_TEXT, font=self.text_font)
		self.start_lbl.pack()

	def init_end_page(self):

		# create page
		frame = Frame(self.central_frame)
		self.frames["EndPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# text
		end_text = END_PAGE_TEXT
		self.end_lbl = Label(self.frames["EndPage"] , text=end_text, font=self.text_font)
		self.end_lbl.pack()

	def init_pages(self):
		self.frames = {}
		#frame_names = ["StartPage", "NumComposantsPage", "ProblemePage", "EndPage"]

		# put all of the pages in the same location;
		# the one on the top of the stacking order
		# will be the one that is visible.

		self.init_start_page()
		self.init_composants_page()
		self.init_probleme_page()
		self.init_end_page()

		# test page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["TestPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# test page
		test_text = "testy page"
		# text
		self.test_lbl = Label(self.frames["TestPage"] , text=test_text, font=self.text_font)
		self.test_lbl.pack()

	def add_new_capteur(self):
		print("kkkk test")
		toniolo = Add_new_capteur_window()

	def next_page(self):
		### go to next page
		if(self.current_page=="StartPage"):
			self.show_frame("NumComposantsPage")
		elif(self.current_page=="NumComposantsPage"):
			self.show_frame("ProblemePage")
		elif(self.current_page=="ProblemePage"):
			self.show_frame("TestPage")
		elif(self.current_page=="TestPage"):
			self.show_frame("EndPage")

	def previous_page(self):
		### go to previous page
		if(self.current_page=="NumComposantsPage"):
			self.show_frame("StartPage")
		elif(self.current_page=="ProblemePage"):
			self.show_frame("NumComposantsPage")
		elif(self.current_page=="TestPage"):
			self.show_frame("ProblemePage")
		elif(self.current_page=="EndPage"):
			self.show_frame("TestPage")

	def quit(self):

		#  save simulation parameters
		save_parameters(params)
		# close window
		self.root.destroy()