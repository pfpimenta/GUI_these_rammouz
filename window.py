#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
from send2trash import send2trash
from convenience import *
from Add_new_capteur_window import *
from Error_window import *



# global variable with the simulation parameters 
params = {}
params['numCapteurs'] = 0
params['numADCs'] = 0
params['numMicroprocesseurs'] = 0
params['numMemoires'] = 0
params['numModulesRadiofrequence'] = 0



class window():

	def __init__(self):
		
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
		#self.current_page = page_name
		self.update_buttons()
		
	def update_buttons(self):
		# no back button in start page
		if(self.frame_names[self.current_page]=="StartPage"):
			self.back_button.grid_forget()
		else:
			self.back_button.grid(column=1, row=4, sticky=E)

		# next button becomes Done button in end page
		if(self.frame_names[self.current_page]=="EndPage"):
			self.next_button.config(text="Done", command=self.quit)
		else:
			self.next_button.config(text="Next", command=self.next_page)
		
	def init_choose_scenario_page(self):

		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["ScenariosPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Choose scenario to simulate"
		self.test_lbl = Label(self.frames["ScenariosPage"] , text=text, font=self.text_font)
		self.test_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.frames["ScenariosPage"], height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.frames["ScenariosPage"])
		frame_for_entries.grid(row=2, column=0)

		# radio button to choose scenario
		MODES = [
			("Scenario 1", "1"),
			("Scenario 2", "2"),
			("Scenario 3", "3"),
			("Scenario 4", "4")
		]

		self.scenarioString = StringVar()
		self.scenarioString.set("1") # initialize

		for text, mode in MODES:
			b = Radiobutton(frame_for_entries, text=text,
							variable=self.scenarioString, value=mode)
			b.pack(anchor=W)

	def init_capteurs_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["CapteursPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Add new capteur \n #TODO"
		self.test_lbl = Label(self.frames["CapteursPage"] , text=text, font=self.text_font)
		self.test_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.frames["CapteursPage"], height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		self.capteur_listbox = Listbox(self.frames["CapteursPage"])
		self.capteur_listbox.grid(column=1, row=1)
		#self.capteur_listbox.pack()

		self.update_capteur_list()

		buttons_frame = Frame(self.frames["CapteursPage"])
		buttons_frame.grid(row=1, column=2)

		self.add_capteur_button = Button(buttons_frame, text = "Add new capteur", command=self.add_new_capteur)
		self.add_capteur_button.grid(column=1, row=1, sticky='news')

		self.remove_capteur_button = Button(buttons_frame, text = "Remove selected capteur", command=self.remove_selected_capteur)
		self.remove_capteur_button.grid(column=1, row=2, sticky='news')

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
		self.frame_names = ["StartPage", "ScenariosPage", "CapteursPage",  "EndPage"] # ordered
		# "TestPage",
		self.current_page = 0
		self.numPages = len(self.frame_names)
		#print("DEBUG numPages: {}".format(self.numPages)) #DEBUG

		# put all of the pages in the same location;
		# the one on the top of the stacking order
		# will be the one that is visible.

		self.init_start_page()
		self.init_choose_scenario_page()
		self.init_capteurs_page()
		self.init_end_page()

	def update_capteur_list(self):
		# to be called when loading CapteursPage or after adding/removing a new capteur
		
		#print("\nDEBUG update_capteur_list called\n")
		components_folder_path = os.getcwd() + "/components/"
		files = os.listdir(components_folder_path) # list of files in 'data_path' folder
		#print("files in components folder : {}".format(files))
		capteur_files = [ f for f in files if 'capteur' in f] # get only capteur files

		# print("DEBUG capteur_listbox items:") # DEBUG
		# print(self.capteur_listbox.get(0, END)) # DEBUG

		# iterate through all capteur files saved in the components folder
		for capteur_filename in capteur_files:
			capteur_name = capteur_filename[8:-7] # ex: "capteur_example.pickle" -> "example"

			# if a capteur is saved but not on the list, add it to the list
			if(capteur_name not in self.capteur_listbox.get(0, END)):
				self.capteur_listbox.insert(END, capteur_name)

	def add_new_capteur(self):
		# (self.add_capteur_button command)
		# opens window to add item to the capteur list in the CapteursPages
		toniolow = Add_new_capteur_window(parent=self)

	def remove_selected_capteur(self):
		# (self.remove_capteur_button command)
		# removes selected capteur in the list and deletes its file
		
		# get name of capteur and corresponding filename
		capteur_name = self.capteur_listbox.get(ANCHOR)
		components_folder_path = os.getcwd() + "/components/"
		capteur_filename = components_folder_path + "capteur_"+ capteur_name + ".pickle"

		# delete file containing the capteur parameters
		#os.remove(capteur_filename)
		send2trash(capteur_filename)

		# delete item from listbox
		self.capteur_listbox.delete(ANCHOR)
		
		print("DEBUG (remove_selected_capteur) removed : {}".format(capteur_filename)) # DEBUG
		
	def changeScenario(self):
		scenario = self.scenarioString.get()

		if(scenario == "1"):
			# scenario 1
			## variables : Autonomie, Source d’énergie
			## parametres : Périodes de déconnexion, Composants, Configuration
			self.frame_names = ["StartPage", "ScenariosPage", "CapteursPage",  "EndPage"] # ordered

		elif(scenario == "2"):
			# TODO TO DO 

			# scenario 2
			## variables : Autonomie
			## parametres : Périodes de déconnexion, Source d’énergie, Composants, Configuration
			#self.frame_names = ["StartPage", "ScenariosPage", "????"] # ordered
			toniolo_error = Error_window()

		elif(scenario == "3"):
			# TODO TO DO 

			# scenario 3
			## variables : Périodes de déconnexion
			## parametres : Autonomie, Source d’énergie, Composants, Configuration
			#self.frame_names = ["StartPage", "ScenariosPage", "????"] # ordered
			toniolo_error = Error_window()

		elif(scenario == "4"):
			# TODO TO DO 

			# scenario 4
			## variables : Source d’énergie, Composants, Configuration
			## parametres : Autonomie, Périodes de déconnexion 
			#self.frame_names = ["StartPage", "ScenariosPage", "????"] # ordered
			toniolo_error = Error_window()

		else:
			print("ERROR : scenario not recoognized")

		# update numPages
		self.numPages = len(self.frame_names)

	def next_page(self):
		### go to next page

		#print("DEBUG next page... current_page: {}, current_page name: {}".format(self.current_page, self.frame_names[self.current_page]))
		if(self.frame_names[self.current_page] == "ScenariosPage"):
			#print("DEBUG change scenario... self.scenarioString: {}".format(self.scenarioString.get())) # DEBUG
			self.changeScenario()

		if(self.current_page == self.numPages-1):
			# is already in last page
			print("ERROR: already in last page: {} == {}".format(self.current_page, self.numPages-1))
		else:
			self.current_page = self.current_page + 1
			self.show_frame(self.frame_names[self.current_page])

	def previous_page(self):
		### go to previous page

		if(self.current_page == 0):
			# is already in first page
			print("ERROR: already in first page")
			pass
		else:
			self.current_page = self.current_page - 1
			self.show_frame(self.frame_names[self.current_page])

	def quit(self):

		#  save simulation parameters
		save_parameters(params)
		# close window
		self.root.destroy()