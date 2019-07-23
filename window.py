#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
from send2trash import send2trash
import pickle
import os
from PIL import ImageTk
import PIL.Image
from convenience import *
from Add_new_capteur_window import *
from Add_new_ADC_window import *
from Add_new_MSP_window import *
from Add_new_memory_window import *
from Add_new_MRF_window import *
#from ProblemePage import *
from Error_window import *


# main window of the GUI
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

		if(page_name == "ProblemePage2"):
			self.update_component_lists()

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
		self.test_lbl = Label(self.frames["ScenariosPage"] , text=text, font=font_titles)
		self.test_lbl.grid(row=0, column=0, sticky=W+E)

		pad_frame = Frame(self.frames["ScenariosPage"], height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.frames["ScenariosPage"])
		frame_for_entries.grid(row=2, column=0, sticky=W+E)

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
		
		# TODO !!!!!!!!!!!!!!!!!!!!!!!!! scenarios image
		#img = ImageTk.PhotoImage(PIL.Image.open(os.getcwd() + "/scenarios_resized.png"))
		#img = ImageTk.PhotoImage(PIL.Image.open("/home/pimenta/GUI_these_rammouz/scenarios_resized.jpg"))
		#panel = Label(self.frames["ScenariosPage"], image = img)
		#panel = Label(self.frames["ScenariosPage"] , text="DEBUGGGG", font=font_titles) # DEBUG
		#panel.grid(row=2, column=1)#, sticky=W+E)
		#panel.pack(side = "bottom", fill = "both", expand = "yes")

	def init_capteurs_page(self):
		
		# create page
		frame = Frame(self.central_frame)#, controller=self)
		self.frames["CapteursPage"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Capteurs"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["CapteursPage"] , text=text, font=font_titles)
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

		text = "Analog-Digital Converters"# \n (texto explicando algo? sei la)\n #TODO "
		self.test_lbl = Label(self.frames["ADCPage"] , text=text, font=font_titles)
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
		self.test_lbl = Label(self.frames["MemoryPage"] , text=text, font=font_titles)
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
		self.test_lbl = Label(self.frames["MSPPage"] , text=text, font=font_titles)
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
		self.test_lbl = Label(self.frames["MRFPage"] , text=text, font=font_titles)
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

	def init_probleme_page_1(self):

		# create page
		frame = Frame(self.central_frame)
		#frame = ProblemePage(self)
		self.frames["ProblemePage1"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Problem configuration"
		self.test_lbl = Label(self.frames["ProblemePage1"] , text=text, font=font_titles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["ProblemePage1"], height=30)
		pad_frame.pack()

		frame_for_entries = Frame(self.frames["ProblemePage1"])
		frame_for_entries.pack()

		current_row = 0

		# Configuration du reseau  (label)
		pad_subtitle = Frame(frame_for_entries, height=10, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1
		lbl_subtitle = Label(frame_for_entries, text="Configuration du reseau ", font=font_subtitles)
		lbl_subtitle.grid(column=1, row=current_row, columnspan = 2, sticky=W)
		current_row = current_row + 1

		### Nombre de noeuds
		lbl_num_noeuds = Label(frame_for_entries, text="Nombre de noeuds ", font=font_params)
		lbl_num_noeuds.grid(column=1, row=current_row)

		# TODO : delete these two lines and accept more than 1 noeud
		lbl_temp = Label(frame_for_entries, text=" 1 ", font=font_params, relief=SUNKEN)
		lbl_temp.grid(column=2, row=current_row, sticky=W+E)

		#self.entry_num_noeuds = Entry(frame_for_entries)
		#self.entry_num_noeuds.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Algorithm de connexion
		lbl_alg_connexion = Label(frame_for_entries, text="Algorithm de connexion ", font=font_params)
		lbl_alg_connexion.grid(column=1, row=current_row)

		OPTIONS = ["continu", "synchonise"]
		var = StringVar(frame_for_entries)
		var.set(OPTIONS[0]) # default value

		self.option_alg_connexion = OptionMenu(frame_for_entries, var, *OPTIONS)
		self.option_alg_connexion.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### Octets par mesure
		lbl_octets_par_mesure = Label(frame_for_entries, text="Octets par mesure (o) ", font=font_params)
		lbl_octets_par_mesure.grid(column=1, row=current_row)

		self.entry_octets_par_mesure = Entry(frame_for_entries)
		self.entry_octets_par_mesure.grid(column=2, row=current_row)
		current_row = current_row + 1
	
	def init_probleme_page_2(self):

		# create page
		frame = Frame(self.central_frame)
		#frame = ProblemePage(self)
		self.frames["ProblemePage2"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Problem configuration"
		self.test_lbl = Label(self.frames["ProblemePage2"] , text=text, font=font_titles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["ProblemePage2"], height=30)
		pad_frame.pack()

		frame_for_entries = Frame(self.frames["ProblemePage2"])
		frame_for_entries.pack()

		current_row = 0

		# Constitution du noeud  (label)
		pad_subtitle = Frame(frame_for_entries, height=5, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1
		lbl_subtitle = Label(frame_for_entries, text="Constitution du noeud ", font=font_subtitles)
		lbl_subtitle.grid(column=1, row=current_row, columnspan = 2, sticky=W)
		current_row = current_row + 1

		### Noeud d'interet
		lbl_noeud_dinteret = Label(frame_for_entries, text="Noeud d'interet ", font=font_params)
		lbl_noeud_dinteret.grid(column=1, row=current_row)

		# TODO : delete these two lines and accept more than 1 noeud
		lbl_temp = Label(frame_for_entries, text=" 1 ", font=font_params, relief=SUNKEN)
		lbl_temp.grid(column=2, row=current_row, sticky=W+E)

		#self.entry_noeud_dinteret = Entry(frame_for_entries)
		#self.entry_noeud_dinteret.grid(column=2, row=current_row)
		current_row = current_row + 1

		### choix Capteur
		lbl_capteur = Label(frame_for_entries, text="Capteur ", font=font_params)
		lbl_capteur.grid(column=1, row=current_row)

		capteur_list = list(self.capteur_listbox.get(0, END))
		self.capteur_list_var = StringVar(frame_for_entries)
		self.capteur_list_var.set(capteur_list[0]) # default value

		self.option_capteur = OptionMenu(frame_for_entries, self.capteur_list_var, *capteur_list)
		self.option_capteur.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### choix ADC
		lbl_ADC = Label(frame_for_entries, text="ADC ", font=font_params)
		lbl_ADC.grid(column=1, row=current_row)
		
		ADC_list = list(self.ADC_listbox.get(0, END))
		self.ADC_list_var = StringVar(frame_for_entries)
		self.ADC_list_var.set(ADC_list[0]) # default value

		self.option_ADC = OptionMenu(frame_for_entries, self.ADC_list_var, *ADC_list)
		self.option_ADC.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### choix Microprocesseur
		lbl_MSP = Label(frame_for_entries, text="Microprocesseur ", font=font_params)
		lbl_MSP.grid(column=1, row=current_row)

		MSP_list = list(self.MSP_listbox.get(0, END))
		self.MSP_list_var = StringVar(frame_for_entries)
		self.MSP_list_var.set(MSP_list[0]) # default value

		self.option_MSP = OptionMenu(frame_for_entries, self.MSP_list_var, *MSP_list)
		self.option_MSP.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### choix Memoire
		lbl_memoire = Label(frame_for_entries, text="Memoire ", font=font_params)
		lbl_memoire.grid(column=1, row=current_row)

		memory_list = list(self.memory_listbox.get(0, END)) 
		self.memory_list_var = StringVar(frame_for_entries)
		self.memory_list_var.set(memory_list[0]) # default value

		self.option_memory = OptionMenu(frame_for_entries, self.memory_list_var, *memory_list)
		self.option_memory.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### choix Module Radio-Frequence
		lbl_MRF = Label(frame_for_entries, text="Module Radio-Frequence ", font=font_params)
		lbl_MRF.grid(column=1, row=current_row)

		MRF_list = list(self.MRF_listbox.get(0, END)) 
		self.MRF_list_var = StringVar(frame_for_entries)
		self.MRF_list_var.set(MRF_list[0]) # default value

		self.option_MRF = OptionMenu(frame_for_entries, self.MRF_list_var, *MRF_list)
		self.option_MRF.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### Periode de mesure
		lbl_periode_mesure = Label(frame_for_entries, text="Periode de mesure (min) ", font=font_params)
		lbl_periode_mesure.grid(column=1, row=current_row)

		self.entry_periode_mesure = Entry(frame_for_entries)
		self.entry_periode_mesure.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Frequence de traitement
		lbl_freq_traitement = Label(frame_for_entries, text="Frequence de traitement (MHz) ", font=font_params)
		lbl_freq_traitement.grid(column=1, row=current_row)

		self.entry_freq_traitement = Entry(frame_for_entries)
		self.entry_freq_traitement.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Frequence d'echantillonage
		lbl_freq_echantillonage = Label(frame_for_entries, text="Frequence d'echantillonage (Hz) ", font=font_params)
		lbl_freq_echantillonage.grid(column=1, row=current_row)

		self.entry_freq_echantillonage = Entry(frame_for_entries)
		self.entry_freq_echantillonage.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Puissance de transmission
		lbl_puissance_transmission = Label(frame_for_entries, text="Puissance de transmission (?) ", font=font_params)
		lbl_puissance_transmission.grid(column=1, row=current_row)

		self.entry_puissance_transmission = Entry(frame_for_entries)
		self.entry_puissance_transmission.grid(column=2, row=current_row)
		current_row = current_row + 1

		# la capacite de la source est une variable dans le scenario 1 !
		# ### Capacite de la source
		# lbl_capacite_source = Label(frame_for_entries, text="Capacite de la source (mAh) ", font=font_params)
		# lbl_capacite_source.grid(column=1, row=current_row)

		# self.entry_capacite_source = Entry(frame_for_entries)
		# self.entry_capacite_source.grid(column=2, row=current_row)
		# current_row = current_row + 1

	def init_probleme_page_3(self):

		# create page
		frame = Frame(self.central_frame)
		#frame = ProblemePage(self)
		self.frames["ProblemePage3"] = frame
		frame.grid(row=0, column=0, sticky="nsew")

		text = "Problem configuration"
		self.test_lbl = Label(self.frames["ProblemePage3"] , text=text, font=font_titles)
		self.test_lbl.pack()

		pad_frame = Frame(self.frames["ProblemePage3"], height=30)
		pad_frame.pack()

		frame_for_entries = Frame(self.frames["ProblemePage3"])
		frame_for_entries.pack()

		current_row = 0

		# l'autonomie du noeud est une variable dans le scenario 1 !
		# ### Autonomie du noeud
		# pad_subtitle = Frame(frame_for_entries, height=5, bg="", colormap="new")
		# pad_subtitle.grid(column=0, row=current_row)
		# current_row = current_row + 1

		# lbl_autonomie_noeud = Label(frame_for_entries, text="Autonomie du noeud (jours) ", font=font_params)
		# lbl_autonomie_noeud.grid(column=1, row=current_row)

		# self.entry_autonomie_noeud = Entry(frame_for_entries)
		# self.entry_autonomie_noeud.grid(column=2, row=current_row)
		# current_row = current_row + 1

		### Duree du monitoring
		pad_subtitle = Frame(frame_for_entries, height=5, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1

		lbl_duree_monitoring = Label(frame_for_entries, text="Duree du monitoring (jours) ", font=font_params)
		lbl_duree_monitoring.grid(column=1, row=current_row)

		self.entry_duree_monitoring = Entry(frame_for_entries)
		self.entry_duree_monitoring.grid(column=2, row=current_row)
		current_row = current_row + 1

		### choix Routine de vie du patient (Etat)
		lbl_routine = Label(frame_for_entries, text="Routine de vie du patient ", font=font_params)
		lbl_routine.grid(column=1, row=current_row)

		OPTIONS = [
			"predefini",
			"aleatoire",
			"non connu"
		]

		var = StringVar(frame_for_entries)
		var.set(OPTIONS[0]) # default value

		self.option_routine = OptionMenu(frame_for_entries, var, *OPTIONS)
		self.option_routine.grid(column=2, row=current_row, sticky = W+E)
		current_row = current_row + 1

		### Periodes de deconnexion quotidiennes (borne inferieure et superieure)
		lbl_periodes_deconnexion = Label(frame_for_entries, text="Periodes de deconnexion quotidiennes ", font=font_params)
		lbl_periodes_deconnexion.grid(column=1, row=current_row)
		
		# TODO
		lbl_TODO = Label(frame_for_entries, text=" // TODO", font=font_params)
		lbl_TODO.grid(column=2, row=current_row)

		#frame_for_borne = Frame(frame_for_entries)
		#frame_for_borne.grid(row=2, column=current_row)

		#self.entry_borne_inf = Entry(frame_for_borne)
		#self.entry_borne_inf.grid(column=0)
		#self.entry_borne_sup = Entry(frame_for_borne)
		#self.entry_borne_sup.grid(column=1)
		current_row = current_row + 1

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
		self.end_lbl = Label(self.frames["EndPage"] , text=end_text, font=font_titles)
		self.end_lbl.pack()

	def init_pages(self):
		self.frames = {}
		self.frame_names = PAGE_NAMES_SCENARIO_1
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
		self.init_probleme_page_1()
		self.init_probleme_page_2()
		self.init_probleme_page_3()
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

		# iterate through all MRF files saved in the components folder
		for MRF_filename in MRF_files:
			MRF_name = MRF_filename[4:-7] # ex: "MRF_example.pickle" -> "example"

			# if a MRF is saved but not on the list, add it to the list
			if(MRF_name not in self.MRF_listbox.get(0, END)):
				self.MRF_listbox.insert(END, MRF_name)

		# print("DEBUG MRF_listbox items:") # DEBUG
		# print(self.MRF_listbox.get(0, END)) # DEBUG # tuple

	def update_component_lists(self):
		# updates the component lists and the option menus in ProblemePage2
		
		## update listboxes by looking inside the components folder
		self.update_capteur_list()
		self.update_ADC_list()
		self.update_memory_list()
		self.update_MSP_list()
		self.update_MRF_list()

		## update the option menus
		# capteur
		capteur_list = list(self.capteur_listbox.get(0, END))
		menu = self.option_capteur["menu"]
		menu.delete(0, "end")
		for string in capteur_list:
			menu.add_command(label=string, 
								command=lambda value=string: self.capteur_list_var.set(value))
		# ADC
		ADC_list = list(self.ADC_listbox.get(0, END))
		menu = self.option_ADC["menu"]
		menu.delete(0, "end")
		for string in ADC_list:
			menu.add_command(label=string, 
								command=lambda value=string: self.ADC_list_var.set(value))
		# memory
		memory_list = list(self.memory_listbox.get(0, END))
		menu = self.option_memory["menu"]
		menu.delete(0, "end")
		for string in memory_list:
			menu.add_command(label=string, 
								command=lambda value=string: self.memory_list_var.set(value))
		# MSP
		MSP_list = list(self.MSP_listbox.get(0, END))
		menu = self.option_MSP["menu"]
		menu.delete(0, "end")
		for string in MSP_list:
			menu.add_command(label=string, 
								command=lambda value=string: self.MSP_list_var.set(value))
		# MRF
		MRF_list = list(self.MRF_listbox.get(0, END))
		menu = self.option_MRF["menu"]
		menu.delete(0, "end")
		for string in MRF_list:
			menu.add_command(label=string, 
								command=lambda value=string: self.MRF_list_var.set(value))

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
			self.frame_names = PAGE_NAMES_SCENARIO_1

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

	def getProblemeParameters(self):
		# gets all the problem configuration parameters and puts it into a dict
		# (called by getSimulationParameters)

		problem_params = {}

		###### list of the params:
		### Configuration du reseau
		# nombre de noeuds
		# algorithm connexion
		# octets par mesure

		problem_params["num_noeuds"] = "1"
		problem_params["alg_connexion"] = self.option_alg_connexion.get() # TODO ????
		problem_params["octets_par_mesure"] = self.entry_octets_par_mesure.get()

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

		problem_params["noeud_dinteret"] = self.entry_noeud_dinteret.get()
		problem_params["capteur"] = self.option_capteur.get()
		problem_params["ADC"] = self.option_ADC.get()
		problem_params["memory"] = self.option_memory.get()
		problem_params["MSP"] = self.option_MSP.get()
		problem_params["MRF"] = self.option_MRF.get()
		problem_params["periode_mesure"] = self.entry_periode_mesure.get()
		problem_params["freq_traitement"] = self.entry_freq_traitement.get()
		problem_params["freq_echantillonage"] = self.entry_freq_echantillonage.get()
		problem_params["puissance_transmission"] = self.entry_puissance_transmission.get()

		### Duree du monitoring

		### Routine de vie du patient
		# choix Etat (routine)
		# periodes de deconnexion quotidiennes (borne inferieure et superieure)

		problem_params["duree_monitoring"] = self.entry_duree_monitoring.get()
		problem_params["routine"] = self.option_routine.get()
		# periodes de deconnexion # TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		
	def getSimulationParameters(self):
		# gets all the simulation parameters and puts it into a dict

		params = {}
		params["capteur"] = getCapteur(self.capteur_list_var.get())
		params["ADC"] = getADC(self.ADC_list_var.get())
		params["memory"] = getMemory(self.memory_list_var.get())
		params["MSP"] = getMSP(self.MSP_list_var.get())
		params["MRF"] = getMRF(self.MRF_list_var.get())
		params["Probleme"] = self.getProblemeParameters()
		return params

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

		params = self.getSimulationParameters()
		print(params)
		#  save simulation parameters
		#save_parameters(params)
		# close window
		self.root.destroy()