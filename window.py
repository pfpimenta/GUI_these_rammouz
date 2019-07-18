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
from Add_new_ADC_window import *
from Add_new_MSP_window import *
from Add_new_memory_window import *
from Add_new_MRF_window import *
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
		self.root.title("GUI - these Rammouz")
		#self.root.geometry('800x600')
		#self.root.configure(background="black")
		### set text font:
		self.text_font = tkfont.Font(family='Verdana', size=13)
		### central frame (where the pages are placed)
		self.central_frame = Frame(self.root, width=500, height=500)
		self.central_frame.grid(column=2, row=2)
		### Next/Done button
		self.next_button = Button(self.root, text = "Next", command=self.next_page)
		self.next_button.grid(column=4, row=4, sticky=E)
		### Back button (previous page)
		self.back_button = Button(self.root, text = "Back", command=self.previous_page)
		self.back_button.grid(column=1, row=4, sticky=E)
		### padding
		pad_frame_top_1 = Frame(self.root,width=50, height=30)
		pad_frame_top_1.grid(column=0, row=0)
		pad_frame_top_2 = Frame(self.root, width=50, height=30)
		pad_frame_top_2.grid(column=1, row=1)
		pad_frame_mid = Frame(self.root, width=50, height=30)
		pad_frame_mid.grid(column=3, row=3)
		pad_frame_bottom = Frame(self.root, width=30, height=25)
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
		self.test_lbl = Label(self.frames["ScenariosPage"] , text=text, font=font_subtitles)
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

		text = "Capteurs"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["CapteursPage"] , text=text, font=font_subtitles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["CapteursPage"], height=30)
		pad_frame.pack()


		listbox_buttons_frame = Frame(self.frames["CapteursPage"])
		listbox_buttons_frame.pack()

		self.capteur_listbox = Listbox(listbox_buttons_frame, height=15, width=20)
		self.capteur_listbox.grid(column=0, row=0)

		self.update_capteur_list()

		buttons_frame = Frame(listbox_buttons_frame)#(self.frames["CapteursPage"])
		buttons_frame.grid(column=1, row=0)

		self.add_capteur_button = Button(buttons_frame, text = "Add new capteur_", command=self.add_new_capteur)
		self.add_capteur_button.grid(column=1, row=1, sticky='news')

		self.remove_capteur_button = Button(buttons_frame, text = "Remove selected capteur", command=self.remove_selected_capteur)
		self.remove_capteur_button.grid(column=1, row=2, sticky='news')

	def init_ADC_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["ADCPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Analog-Digial Converters"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["ADCPage"] , text=text, font=font_subtitles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["ADCPage"], height=30)
		pad_frame.pack()


		listbox_buttons_frame = Frame(self.frames["ADCPage"])
		listbox_buttons_frame.pack()

		self.ADC_listbox = Listbox(listbox_buttons_frame, height=15, width=20)
		self.ADC_listbox.grid(column=0, row=0)

		self.update_ADC_list()

		buttons_frame = Frame(listbox_buttons_frame)#(self.frames["ADCPage"])
		buttons_frame.grid(column=1, row=0)

		self.add_ADC_button = Button(buttons_frame, text = "Add new ADC", command=self.add_new_ADC)
		self.add_ADC_button.grid(column=1, row=1, sticky='news')

		self.remove_ADC_button = Button(buttons_frame, text = "Remove selected ADC", command=self.remove_selected_ADC)
		self.remove_ADC_button.grid(column=1, row=2, sticky='news')

	def init_memory_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["MemoryPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Memories"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["MemoryPage"] , text=text, font=font_subtitles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["MemoryPage"], height=30)
		pad_frame.pack()


		listbox_buttons_frame = Frame(self.frames["MemoryPage"])
		listbox_buttons_frame.pack()

		self.memory_listbox = Listbox(listbox_buttons_frame, height=15, width=20)
		self.memory_listbox.grid(column=0, row=0)

		self.update_memory_list()

		buttons_frame = Frame(listbox_buttons_frame)#(self.frames["MemoryPage"])
		buttons_frame.grid(column=1, row=0)

		self.add_memory_button = Button(buttons_frame, text = "Add new memory", command=self.add_new_memory)
		self.add_memory_button.grid(column=1, row=1, sticky='news')

		self.remove_memory_button = Button(buttons_frame, text = "Remove selected memory", command=self.remove_selected_memory)
		self.remove_memory_button.grid(column=1, row=2, sticky='news')

	def init_MSP_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["MSPPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Microprocesseurs"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["MSPPage"] , text=text, font=font_subtitles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["MSPPage"], height=30)
		pad_frame.pack()


		listbox_buttons_frame = Frame(self.frames["MSPPage"])
		listbox_buttons_frame.pack()

		self.MSP_listbox = Listbox(listbox_buttons_frame, height=15, width=20)
		self.MSP_listbox.grid(column=0, row=0)

		self.update_MSP_list()

		buttons_frame = Frame(listbox_buttons_frame)#(self.frames["MSPPage"])
		buttons_frame.grid(column=1, row=0)

		self.add_MSP_button = Button(buttons_frame, text = "Add new MSP", command=self.add_new_MSP)
		self.add_MSP_button.grid(column=1, row=1, sticky='news')

		self.remove_MSP_button = Button(buttons_frame, text = "Remove selected MSP", command=self.remove_selected_MSP)
		self.remove_MSP_button.grid(column=1, row=2, sticky='news')

	def init_MRF_page(self):
		# MRF = Module Radio-Frequence
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["MRFPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Modules Radio-Frequence"#\n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["MRFPage"] , text=text, font=font_subtitles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["MRFPage"], height=30)
		pad_frame.pack()


		listbox_buttons_frame = Frame(self.frames["MRFPage"])
		listbox_buttons_frame.pack()

		self.MRF_listbox = Listbox(listbox_buttons_frame, height=15, width=20)
		self.MRF_listbox.grid(column=0, row=0)

		self.update_MRF_list()

		buttons_frame = Frame(listbox_buttons_frame)#(self.frames["MRFPage"])
		buttons_frame.grid(column=1, row=0)

		self.add_MRF_button = Button(buttons_frame, text = "Add new MRF", command=self.add_new_MRF)
		self.add_MRF_button.grid(column=1, row=1, sticky='news')

		self.remove_MRF_button = Button(buttons_frame, text = "Remove selected MRF", command=self.remove_selected_MRF)
		self.remove_MRF_button.grid(column=1, row=2, sticky='news')

	def init_probleme_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["ProblemePage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Probleme ...? \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["ProblemePage"] , text=text, font=self.text_font)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["ProblemePage"], height=30)
		pad_frame.pack()

		### Configuration du reseau
		# nombre de noeuds
		# algorithm connexion
		# octets par mesure

		### Constitution du noeud
		# noeud d'interet
		# choix Capteur
		# choix ADC
		# choix Microprocesseur
		# choix Memoire
		# choix Module Radio-Frequence
		# Periode de mesure (x2 ???)
		# Frequence de traitement
		# Frequence d'echantillonage
		# Puissance de transmission

		### Autonomie du noeud

		### Duree du monitoring

		### Routine de vie du patient
		# choix Etat
		# periodes de deconnexion quotidiennes (borne inferieure et superieure)

	def init_start_page(self):

		# create page
		frame = Frame(self.central_frame)
		self.frames["StartPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# text
		self.start_lbl = Label(self.frames["StartPage"] , text=START_PAGE_TEXT, font=font_params)
		self.start_lbl.pack()
		pad_frame_top_1 = Frame(self.frames["StartPage"], height=100)
		pad_frame_top_1.pack() #.grid(column=0, row=0)

		self.thesis_link_lbl = Label(self.frames["StartPage"] , text=THESIS_LINK, font=font_params)
		self.thesis_link_lbl.pack()

	def init_end_page(self):

		# create page
		frame = Frame(self.central_frame)
		self.frames["EndPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		# text
		end_text = END_PAGE_TEXT
		self.end_lbl = Label(self.frames["EndPage"] , text=end_text, font=font_params)
		self.end_lbl.pack()

	def init_pages(self):
		self.frames = {}
		self.frame_names = ["StartPage", "ScenariosPage", "CapteursPage", "ADCPage", "MemoryPage", "MSPPage", "MRFPage", "EndPage"] # ordered
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
		self.init_ADC_page()
		self.init_memory_page()
		self.init_MSP_page()
		self.init_MRF_page()
		#self.init_probleme_page()
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

	def update_ADC_list(self):
		# to be called when loading ADCPage or after adding/removing a new ADC
		
		#print("\nDEBUG update_ADC_list called\n")
		components_folder_path = os.getcwd() + "/components/"
		files = os.listdir(components_folder_path) # list of files in 'data_path' folder
		#print("files in components folder : {}".format(files))
		ADC_files = [ f for f in files if 'ADC' in f] # get only ADC files

		# print("DEBUG ADC_listbox items:") # DEBUG
		# print(self.ADC_listbox.get(0, END)) # DEBUG

		# iterate through all ADC files saved in the components folder
		for ADC_filename in ADC_files:
			ADC_name = ADC_filename[4:-7] # ex: "ADC_example.pickle" -> "example"

			# if a ACC is saved but not on the list, add it to the list
			if(ADC_name not in self.ADC_listbox.get(0, END)):
				self.ADC_listbox.insert(END, ADC_name)

	def update_memory_list(self):
		# to be called when loading MemoryPage or after adding/removing a new memory
		
		#print("\nDEBUG update_memory_list called\n")
		components_folder_path = os.getcwd() + "/components/"
		files = os.listdir(components_folder_path) # list of files in 'data_path' folder
		#print("files in components folder : {}".format(files))
		memory_files = [ f for f in files if 'memory' in f] # get only memory files

		# print("DEBUG memory_listbox items:") # DEBUG
		# print(self.memory_listbox.get(0, END)) # DEBUG

		# iterate through all memory files saved in the components folder
		for memory_filename in memory_files:
			memory_name = memory_filename[7:-7] # ex: "memory_example.pickle" -> "example"

			# if a memory is saved but not on the list, add it to the list
			if(memory_name not in self.memory_listbox.get(0, END)):
				self.memory_listbox.insert(END, memory_name)

	def update_MSP_list(self):
		# to be called when loading MSPPage or after adding/removing a new MSP (microprocesseur)
		
		#print("\nDEBUG update_MSP_list called\n")
		components_folder_path = os.getcwd() + "/components/"
		files = os.listdir(components_folder_path) # list of files in 'data_path' folder
		#print("files in components folder : {}".format(files))
		MSP_files = [ f for f in files if 'MSP' in f] # get only MSP files

		# print("DEBUG MSP_listbox items:") # DEBUG
		# print(self.MSP_listbox.get(0, END)) # DEBUG

		# iterate through all MSP files saved in the components folder
		for MSP_filename in MSP_files:
			MSP_name = MSP_filename[4:-7] # ex: "MSP_example.pickle" -> "example"

			# if a MSP is saved but not on the list, add it to the list
			if(MSP_name not in self.MSP_listbox.get(0, END)):
				self.MSP_listbox.insert(END, MSP_name)

	def update_MRF_list(self):
		# to be called when loading MRFPage or after adding/removing a new MRF (Module Radio-Frequence)
		
		#print("\nDEBUG update_MRF_list called\n")
		components_folder_path = os.getcwd() + "/components/"
		files = os.listdir(components_folder_path) # list of files in 'data_path' folder
		#print("files in components folder : {}".format(files))
		MRF_files = [ f for f in files if 'MRF' in f] # get only MRF files

		# print("DEBUG MRF_listbox items:") # DEBUG
		# print(self.MRF_listbox.get(0, END)) # DEBUG

		# iterate through all MRF files saved in the components folder
		for MRF_filename in MRF_files:
			MRF_name = MRF_filename[4:-7] # ex: "MRF_example.pickle" -> "example"

			# if a MRF is saved but not on the list, add it to the list
			if(MRF_name not in self.MRF_listbox.get(0, END)):
				self.MRF_listbox.insert(END, MRF_name)

	def add_new_capteur(self):
		# (self.add_capteur_button command)
		# opens window to add item to the capteur list in the CapteursPage
		capteur_window = Add_new_capteur_window(parent=self)

	def add_new_ADC(self):
		# (self.add_ADC_button command)
		# opens window to add item to the ADC list in the ADCPage
		ADC_window = Add_new_ADC_window(parent=self)

	def add_new_MSP(self):
		# (self.add_MSP_button command)
		# opens window to add item to the microprocessers list in the MSPPage
		MSP_window = Add_new_MSP_window(parent=self)  # MSP = Microprocesseur

	def add_new_memory(self):
		# (self.add_memory_button command)
		# opens window to add item to the memory list in the MemoryPage
		memory_window = Add_new_memory_window(parent=self)

	def add_new_MRF(self):
		# (self.add_MRF_button command)
		# opens window to add item to the module_radio_frequence list in the MRFPage
		MRF_window = Add_new_MRF_window(parent=self) # MRF = Module Radio-Frequence

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
		
	def remove_selected_ADC(self):
		# (self.remove_ADC_button command)
		# removes selected ADC in the list and deletes its file
		
		# get name of ADC and corresponding filename
		ADC_name = self.ADC_listbox.get(ANCHOR)
		components_folder_path = os.getcwd() + "/components/"
		ADC_filename = components_folder_path + "ADC_"+ ADC_name + ".pickle"

		# delete file containing the ADC parameters
		#os.remove(ADC_filename)
		send2trash(ADC_filename)

		# delete item from listbox
		self.ADC_listbox.delete(ANCHOR)
		
		print("DEBUG (remove_selected_ADC) removed : {}".format(ADC_filename)) # DEBUG

	def remove_selected_memory(self):
		# (self.remove_memory_button command)
		# removes selected memory in the list and deletes its file
		
		# get name of memory and corresponding filename
		memory_name = self.memory_listbox.get(ANCHOR)
		components_folder_path = os.getcwd() + "/components/"
		memory_filename = components_folder_path + "memory_"+ memory_name + ".pickle"

		# delete file containing the memory parameters
		#os.remove(memory_filename)
		send2trash(memory_filename)

		# delete item from listbox
		self.memory_listbox.delete(ANCHOR)
		
		print("DEBUG (remove_selected_memory) removed : {}".format(memory_filename)) # DEBUG

	def remove_selected_MSP(self):
		# (self.remove_MSP_button command)
		# removes selected MSP in the list and deletes its file
		
		# get name of MSP and corresponding filename
		MSP_name = self.MSP_listbox.get(ANCHOR)
		components_folder_path = os.getcwd() + "/components/"
		MSP_filename = components_folder_path + "MSP_"+ MSP_name + ".pickle"

		# delete file containing the MSP parameters
		#os.remove(MSP_filename)
		send2trash(MSP_filename)

		# delete item from listbox
		self.MSP_listbox.delete(ANCHOR)
		
		print("DEBUG (remove_selected_MSP) removed : {}".format(MSP_filename)) # DEBUG
		
	def remove_selected_MRF(self):
		# (self.remove_MRF_button command)
		# removes selected MRF in the list and deletes its file
		
		# get name of MRF and corresponding filename
		MRF_name = self.MRF_listbox.get(ANCHOR)
		components_folder_path = os.getcwd() + "/components/"
		MRF_filename = components_folder_path + "MRF_"+ MRF_name + ".pickle" # MRF = Module Radio-Frequence

		# delete file containing the MRF parameters
		#os.remove(MRF_filename)
		send2trash(MRF_filename)

		# delete item from listbox
		self.MRF_listbox.delete(ANCHOR)
		
		print("DEBUG (remove_selected_MRF) removed : {}".format(MRF_filename)) # DEBUG
		
	def changeScenario(self):
		scenario = self.scenarioString.get()

		if(scenario == "1"):
			# scenario 1
			## variables : Autonomie, Source d’énergie
			## parametres : Périodes de déconnexion, Composants, Configuration
			self.frame_names = ["StartPage", "ScenariosPage", "CapteursPage", "ADCPage", "MemoryPage", "MSPPage", "MRFPage", "EndPage"] # ordered

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