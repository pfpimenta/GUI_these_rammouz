#!/usr/bin/python
# -*- coding: utf-8 -*-

# window to enter the parameters of a new memory
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
import os
import pickle
from convenience import *
import sys

class Add_new_memory_window():
# window for entering the characteristics of a new memory
# when the Done button is clicked, the memory is saved in a .pickle file

	def __init__(self, parent):
		self.parent = parent

		# windows general layout
		self.init_main_layout(parent.root)

		# init central frame (where are the parameter entries)
		self.init_central_frame()
		
	def init_main_layout(self, parent_window):
		### init window:
		self.root = Toplevel(parent_window)
		self.root.title("Add new memory") # "GUI - these Rammouz"
		### set text font:
		self.text_font = tkfont.Font(family='Verdana', size=13)#, weight="bold", slant="italic")
		### central frame (where the parameter entries are placed)
		self.central_frame = Frame(self.root, width=400, height=300, bg="", colormap="new", relief=SUNKEN)
		self.central_frame.grid(column=2, row=2)
		### Cancel button
		self.cancel_button = Button(self.root, text = "Cancel", command=self.cancel)
		self.cancel_button.grid(column=1, row=4, sticky=E)
		### Done button
		self.done_button = Button(self.root, text = "Done", command=self.done)
		self.done_button.grid(column=4, row=4, sticky=E)
		### padding
		pad_frame_top_1 = Frame(self.root,width=50, height=30, bg="", colormap="new")
		pad_frame_top_1.grid(column=0, row=0)
		pad_frame_top_2 = Frame(self.root, width=50, height=30, bg="", colormap="new")
		pad_frame_top_2.grid(column=1, row=1)
		pad_frame_mid = Frame(self.root, width=50, height=30, bg="", colormap="new")
		pad_frame_mid.grid(column=3, row=3)
		pad_frame_bottom = Frame(self.root, width=30, height=25, bg="", colormap="new")
		pad_frame_bottom.grid(column=10, row=10)

	def init_central_frame(self):
		# text
		text = "Saisissez les parametres de la nouvelle memoire, svp"
		self.text_lbl = Label(self.central_frame, text=text, font=font_params)
		self.text_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.central_frame, height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.central_frame)
		frame_for_entries.grid(row=2, column=0)

		current_row = 0

		### memory name
		lbl_name = Label(frame_for_entries, text="Name", font=font_subtitles)
		lbl_name.grid(column=1, row=current_row, sticky=W)

		self.entry_name = Entry(frame_for_entries)
		self.entry_name.grid(column=2, row=current_row)
		current_row = current_row + 1

		# Fonctionnement  (label)
		pad_subtitle = Frame(frame_for_entries, height=15, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1
		lbl_subtitle = Label(frame_for_entries, text="Fonctionnement ", font=font_subtitles)
		lbl_subtitle.grid(column=1, row=current_row, columnspan = 2, sticky=W)
		current_row = current_row + 1

		### taille
		lbl_taille = Label(frame_for_entries, text="Taille (ko) ", font=font_params)
		lbl_taille.grid(column=1, row=current_row)

		self.entry_taille = Entry(frame_for_entries)
		self.entry_taille.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Octets par instruction
		lbl_octets_intruction = Label(frame_for_entries, text="Octets par instruction (o) ", font=font_params)
		lbl_octets_intruction.grid(column=1, row=current_row)

		self.entry_octets_intruction = Entry(frame_for_entries)
		self.entry_octets_intruction.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Frequence SPI
		lbl_freq_spi = Label(frame_for_entries, text="Frequence SPI (MHz) ", font=font_params)
		lbl_freq_spi.grid(column=1, row=current_row)

		self.entry_freq_spi = Entry(frame_for_entries)
		self.entry_freq_spi.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Octets par ecriture
		lbl_octets_ecriture = Label(frame_for_entries, text="Octets par ecriture (o) ", font=font_params)
		lbl_octets_ecriture.grid(column=1, row=current_row)

		self.entry_octets_ecriture = Entry(frame_for_entries)
		self.entry_octets_ecriture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Duree d'ecriture
		lbl_duree_ecriture = Label(frame_for_entries, text="Duree d'ecriture (us) ", font=font_params)
		lbl_duree_ecriture.grid(column=1, row=current_row)

		self.entry_duree_ecriture = Entry(frame_for_entries)
		self.entry_duree_ecriture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Octets par lecture
		lbl_octets_lecture = Label(frame_for_entries, text="Octets par lecture (o) ", font=font_params)
		lbl_octets_lecture.grid(column=1, row=current_row)

		self.entry_octets_lecture = Entry(frame_for_entries)
		self.entry_octets_lecture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Duree de lecture
		lbl_duree_lecture = Label(frame_for_entries, text="Duree d'lecture (us) ", font=font_params)
		lbl_duree_lecture.grid(column=1, row=current_row)

		self.entry_duree_lecture = Entry(frame_for_entries)
		self.entry_duree_lecture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Octets par effacement
		lbl_octets_effacement = Label(frame_for_entries, text="Octets par effacement (ko) ", font=font_params)
		lbl_octets_effacement.grid(column=1, row=current_row)

		self.entry_octets_effacement = Entry(frame_for_entries)
		self.entry_octets_effacement.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Duree d'effacement
		lbl_duree_effacement = Label(frame_for_entries, text="Duree d'effacement (ms) ", font=font_params)
		lbl_duree_effacement.grid(column=1, row=current_row)

		self.entry_duree_effacement = Entry(frame_for_entries)
		self.entry_duree_effacement.grid(column=2, row=current_row)
		current_row = current_row + 1

		# Transitions  (label)
		pad_subtitle = Frame(frame_for_entries, height=15, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1
		lbl_subtitle = Label(frame_for_entries, text="Transitions ", font=font_subtitles)
		lbl_subtitle.grid(column=1, row=current_row, columnspan = 2, sticky=W)
		current_row = current_row + 1

		### transition basse consomation 1 -> actif
		lbl_trans_basse1_actif = Label(frame_for_entries, text="Basse consomation 1 -> Actif (us) ", font=font_params)
		lbl_trans_basse1_actif.grid(column=1, row=current_row)

		self.entry_trans_basse1_actif = Entry(frame_for_entries)
		self.entry_trans_basse1_actif.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition actif -> basse consomation 1
		lbl_trans_actif_basse1 = Label(frame_for_entries, text="Actif -> Basse consomation 1 (us) ", font=font_params)
		lbl_trans_actif_basse1.grid(column=1, row=current_row)

		self.entry_trans_actif_basse1 = Entry(frame_for_entries)
		self.entry_trans_actif_basse1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition basse consomation 2 -> actif
		lbl_trans_basse2_actif = Label(frame_for_entries, text="Basse consomation 2 -> Actif (us) ", font=font_params)
		lbl_trans_basse2_actif.grid(column=1, row=current_row)

		self.entry_trans_basse2_actif = Entry(frame_for_entries)
		self.entry_trans_basse2_actif.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition actif -> basse consomation 2
		lbl_trans_actif_basse2 = Label(frame_for_entries, text="Actif -> Basse consomation 2 (us) ", font=font_params)
		lbl_trans_actif_basse2.grid(column=1, row=current_row)

		self.entry_trans_actif_basse2 = Entry(frame_for_entries)
		self.entry_trans_actif_basse2.grid(column=2, row=current_row)
		current_row = current_row + 1

		# Consommation  (label)
		pad_subtitle = Frame(frame_for_entries, height=15, bg="", colormap="new")
		pad_subtitle.grid(column=0, row=current_row)
		current_row = current_row + 1
		lbl_subtitle = Label(frame_for_entries, text="Consommation ", font=font_subtitles)
		lbl_subtitle.grid(column=1, row=current_row, columnspan = 2, sticky=W)
		current_row = current_row + 1

		### consomation mode actif
		lbl_conso_actif = Label(frame_for_entries, text="Mode actif (mA) ", font=font_params)
		lbl_conso_actif.grid(column=1, row=current_row)

		self.entry_conso_actif = Entry(frame_for_entries)
		self.entry_conso_actif.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode ecriture
		lbl_conso_ecriture = Label(frame_for_entries, text="Mode ecriture (mA) ", font=font_params)
		lbl_conso_ecriture.grid(column=1, row=current_row)

		self.entry_conso_ecriture = Entry(frame_for_entries)
		self.entry_conso_ecriture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode lecture
		lbl_conso_lecture = Label(frame_for_entries, text="Mode lecture (mA) ", font=font_params)
		lbl_conso_lecture.grid(column=1, row=current_row)

		self.entry_conso_lecture = Entry(frame_for_entries)
		self.entry_conso_lecture.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode effacement
		lbl_conso_effacement = Label(frame_for_entries, text="Mode effacement (mA) ", font=font_params)
		lbl_conso_effacement.grid(column=1, row=current_row)

		self.entry_conso_effacement = Entry(frame_for_entries)
		self.entry_conso_effacement.grid(column=2, row=current_row)
		current_row = current_row + 1
		
		### consomation mode basse consomation 1
		lbl_conso_basse1 = Label(frame_for_entries, text="Mode basse consomation 1 (uA) ", font=font_params)
		lbl_conso_basse1.grid(column=1, row=current_row)

		self.entry_conso_basse1 = Entry(frame_for_entries)
		self.entry_conso_basse1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 2
		lbl_conso_basse2 = Label(frame_for_entries, text="Mode basse consomation 2 (uA) ", font=font_params)
		lbl_conso_basse2.grid(column=1, row=current_row)

		self.entry_conso_basse2 = Entry(frame_for_entries)
		self.entry_conso_basse2.grid(column=2, row=current_row)
		current_row = current_row + 1


	def verify_memory_params(self, memory_params):
		# verify if the parameters of the memory are valid
		if(isinstance(memory_params["name"], str) == False):
			return False
		if(is_number(memory_params["taille"]) == False):
			return False
		if(is_number(memory_params["octets_instruction"]) == False):
			return False
		if(is_number(memory_params["freq_spi"]) == False):
			return False
		if(is_number(memory_params["octets_ecriture"]) == False):
			return False
		if(is_number(memory_params["duree_ecriture"]) == False):
			return False
		if(is_number(memory_params["octets_lecture"]) == False):
			return False
		if(is_number(memory_params["duree_lecture"]) == False):
			return False
		if(is_number(memory_params["octets_effacement"]) == False):
			return False
		if(is_number(memory_params["duree_effacement"]) == False):
			return False
		if(is_number(memory_params["trans_basse1_actif"]) == False):
			return False
		if(is_number(memory_params["trans_actif_basse1"]) == False):
			return False
		if(is_number(memory_params["trans_basse2_actif"]) == False):
			return False
		if(is_number(memory_params["trans_actif_basse2"]) == False):
			return False
		if(is_number(memory_params["conso_actif"]) == False):
			return False
		if(is_number(memory_params["conso_ecriture"]) == False):
			return False
		if(is_number(memory_params["conso_lecture"]) == False):
			return False
		if(is_number(memory_params["conso_effacement"]) == False):
			return False
		if(is_number(memory_params["conso_basse1"]) == False):
			return False
		if(is_number(memory_params["conso_basse2"]) == False):
			return False
		return True # no problems

	def save_memory(self):
		
		# put params into a dict
		memory_params = {}
		# name :
		memory_params["name"] =  self.entry_name.get()
		# fonctionnement :
		memory_params["taille"] =  self.entry_taille.get()
		memory_params["octets_instruction"] =  self.entry_octets_intruction.get()
		memory_params["freq_spi"] =  self.entry_freq_spi.get()
		memory_params["octets_ecriture"] =  self.entry_octets_ecriture.get()
		memory_params["duree_ecriture"] =  self.entry_duree_ecriture.get()
		memory_params["octets_lecture"] =  self.entry_octets_lecture.get()
		memory_params["duree_lecture"] =  self.entry_duree_lecture.get()
		memory_params["octets_effacement"] =  self.entry_octets_effacement.get()
		memory_params["duree_effacement"] =  self.entry_duree_effacement.get()
		# transitions :
		memory_params["trans_basse1_actif"] =  self.entry_trans_basse1_actif.get()
		memory_params["trans_actif_basse1"] =  self.entry_trans_actif_basse1.get()
		memory_params["trans_basse2_actif"] =  self.entry_trans_basse2_actif.get()
		memory_params["trans_actif_basse2"] =  self.entry_trans_actif_basse2.get()
		# consommation : 
		memory_params["conso_actif"] =  self.entry_conso_actif.get()
		memory_params["conso_ecriture"] =  self.entry_conso_ecriture.get()
		memory_params["conso_lecture"] =  self.entry_conso_lecture.get()
		memory_params["conso_effacement"] =  self.entry_conso_effacement.get()
		memory_params["conso_basse1"] =  self.entry_conso_basse1.get()
		memory_params["conso_basse2"] =  self.entry_conso_basse2.get()
		#print("debug memory_params : {}".format(memory_params)) # DEBUG

		if(self.verify_memory_params(memory_params) == False):
			# parameters not valid !
			print("ERROR : memory parameters not valid")
			#sys.exit("ERROR : memory parameters not valid")
		else:
			# create pickle file to save memory params
			components_folder_path = os.getcwd() + "/components/"
			memory_filename = components_folder_path + "memory_" + memory_params["name"] + ".pickle"
			pickling_on = open(memory_filename,"wb")
			pickle.dump(memory_params, pickling_on)
			pickling_on.close()

	def cancel(self):
		self.root.destroy()

	def done(self):
		self.save_memory()
		self.parent.update_memory_list()
		self.root.destroy()
