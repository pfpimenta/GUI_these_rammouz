#!/usr/bin/python
# -*- coding: utf-8 -*-

# window to enter the parameters of a new MRF (Module Radio-Frequence)
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
import os
import pickle
from convenience import *
import sys

class Add_new_MRF_window():
# window for entering the characteristics of a new MRF (Module Radio-Frequence)
# when the Done button is clicked, the MRF is saved in a .pickle file

	def __init__(self, parent):
		self.parent = parent

		# windows general layout
		self.init_main_layout(parent.root)

		# init central frame (where are the parameter entries)
		self.init_central_frame()
		
	def init_main_layout(self, parent_window):
		### init window:
		self.root = Toplevel(parent_window)
		self.root.title("Add new MRF") # "GUI - these Rammouz"
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
		self.text_lbl = Label(self.central_frame, text=text, font=self.text_font)
		self.text_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.central_frame, height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.central_frame)
		frame_for_entries.grid(row=2, column=0)

		current_row = 0

		### MRF name
		lbl_name = Label(frame_for_entries, text="name ")
		lbl_name.grid(column=1, row=current_row)

		self.entry_name = Entry(frame_for_entries)
		self.entry_name.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Connection interval
		lbl_connection_interval = Label(frame_for_entries, text="Connection interval (ms) ")
		lbl_connection_interval.grid(column=1, row=current_row)

		self.entry_connection_interval = Entry(frame_for_entries)
		self.entry_connection_interval.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Advertising interval
		lbl_advertising_interval = Label(frame_for_entries, text="Advertising interval (ms) ")
		lbl_advertising_interval.grid(column=1, row=current_row)

		self.entry_advertising_interval = Entry(frame_for_entries)
		self.entry_advertising_interval.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition basse consomation 1 -> actif
		lbl_trans_basse1_actif = Label(frame_for_entries, text="transition basse consomation 1 -> actif (us) ")
		lbl_trans_basse1_actif.grid(column=1, row=current_row)

		self.entry_trans_basse1_actif = Entry(frame_for_entries)
		self.entry_trans_basse1_actif.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition actif -> basse consomation 1
		lbl_trans_actif_basse1 = Label(frame_for_entries, text="transition actif -> basse consomation 1 (us) ")
		lbl_trans_actif_basse1.grid(column=1, row=current_row)

		self.entry_trans_actif_basse1 = Entry(frame_for_entries)
		self.entry_trans_actif_basse1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition basse consomation 2 -> actif
		lbl_trans_basse2_actif = Label(frame_for_entries, text="transition basse consomation 2 -> actif (us) ")
		lbl_trans_basse2_actif.grid(column=1, row=current_row)

		self.entry_trans_basse2_actif = Entry(frame_for_entries)
		self.entry_trans_basse2_actif.grid(column=2, row=current_row)
		current_row = current_row + 1

		### transition actif -> basse consomation 2
		lbl_trans_actif_basse2 = Label(frame_for_entries, text="transition actif -> basse consomation 2 (us) ")
		lbl_trans_actif_basse2.grid(column=1, row=current_row)

		self.entry_trans_actif_basse2 = Entry(frame_for_entries)
		self.entry_trans_actif_basse2.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Transmission (puissance de transmission == 1)
		lbl_transm_1 = Label(frame_for_entries, text="Transmission (puissance de transmission == 1) (mA) ")
		lbl_transm_1.grid(column=1, row=current_row)

		self.entry_transm_1 = Entry(frame_for_entries)
		self.entry_transm_1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Transmission (puissance de transmission == 7)
		lbl_transm_7 = Label(frame_for_entries, text="Transmission (puissance de transmission == 7) (mA) ")
		lbl_transm_7.grid(column=1, row=current_row)

		self.entry_transm_7 = Entry(frame_for_entries)
		self.entry_transm_7.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Transmission (puissance de transmission == 15)
		lbl_transm_15 = Label(frame_for_entries, text="Transmission (puissance de transmission == 15) (mA) ")
		lbl_transm_15.grid(column=1, row=current_row)

		self.entry_transm_15 = Entry(frame_for_entries)
		self.entry_transm_15.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode reception
		lbl_conso_reception = Label(frame_for_entries, text="consomation mode reception (mA) ")
		lbl_conso_reception.grid(column=1, row=current_row)

		self.entry_conso_reception = Entry(frame_for_entries)
		self.entry_conso_reception.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode actif
		lbl_conso_actif = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif.grid(column=1, row=current_row)

		self.entry_conso_actif = Entry(frame_for_entries)
		self.entry_conso_actif.grid(column=2, row=current_row)
		current_row = current_row + 1
		
		### consomation mode basse consomation 1
		lbl_conso_basse1 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1.grid(column=1, row=current_row)

		self.entry_conso_basse1 = Entry(frame_for_entries)
		self.entry_conso_basse1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 2
		lbl_conso_basse2 = Label(frame_for_entries, text="consomation mode basse consomation 2 (uA) ")
		lbl_conso_basse2.grid(column=1, row=current_row)

		self.entry_conso_basse2 = Entry(frame_for_entries)
		self.entry_conso_basse2.grid(column=2, row=current_row)
		current_row = current_row + 1


	def verify_MRF_params(self, MRF_params):
		# verify if the parameters of the MRF are valid
		if(isinstance(MRF_params["name"], str) == False):
			return False
		if(is_number(MRF_params["connection_interval"]) == False):
			return False
		if(is_number(MRF_params["advertising_interval"]) == False):
			return False
		if(is_number(MRF_params["trans_basse1_actif"]) == False):
			return False
		if(is_number(MRF_params["trans_actif_basse1"]) == False):
			return False
		if(is_number(MRF_params["trans_basse2_actif"]) == False):
			return False
		if(is_number(MRF_params["trans_actif_basse2"]) == False):
			return False
		if(is_number(MRF_params["transm_1"]) == False):
			return False
		if(is_number(MRF_params["transm_7"]) == False):
			return False
		if(is_number(MRF_params["transm_15"]) == False):
			return False
		if(is_number(MRF_params["conso_reception"]) == False):
			return False
		if(is_number(MRF_params["conso_actif"]) == False):
			return False
		if(is_number(MRF_params["conso_basse1"]) == False):
			return False
		if(is_number(MRF_params["conso_basse2"]) == False):
			return False
		return True # no problems

	def save_MRF(self):
		# save the MRF parameters in a pickle file
		
		# put params into a dict
		MRF_params = {}
		# name :
		MRF_params["name"] =  self.entry_name.get()
		# transitions :
		MRF_params["connection_interval"] =  self.entry_connection_interval.get()
		MRF_params["advertising_interval"] =  self.entry_advertising_interval.get()
		MRF_params["trans_basse1_actif"] =  self.entry_trans_basse1_actif.get()
		MRF_params["trans_actif_basse1"] =  self.entry_trans_actif_basse1.get()
		MRF_params["trans_basse2_actif"] =  self.entry_trans_basse2_actif.get()
		MRF_params["trans_actif_basse2"] =  self.entry_trans_actif_basse2.get()
		# consommation
		MRF_params["transm_1"] =  self.entry_transm_1.get()
		MRF_params["transm_7"] =  self.entry_transm_7.get()
		MRF_params["transm_15"] =  self.entry_transm_15.get()
		MRF_params["conso_reception"] =  self.entry_conso_reception.get()
		MRF_params["conso_actif"] =  self.entry_conso_actif.get()
		MRF_params["conso_basse1"] =  self.entry_conso_basse1.get()
		MRF_params["conso_basse2"] =  self.entry_conso_basse2.get()
		#print("debug MRF_params : {}".format(MRF_params)) # DEBUG

		if(self.verify_MRF_params(MRF_params) == False):
			# parameters not valid !
			print("ERROR : MRF parameters not valid")
			#sys.exit("ERROR : MRF parameters not valid")
		else:
			# create pickle file to save MRF params
			components_folder_path = os.getcwd() + "/components/"
			MRF_filename = components_folder_path + "MRF_" + MRF_params["name"] + ".pickle"
			pickling_on = open(MRF_filename,"wb")
			pickle.dump(MRF_params, pickling_on)
			pickling_on.close()

	def cancel(self):
		# Cancel button action
		self.root.destroy()

	def done(self):
		# Done button action
		self.save_MRF()
		self.parent.update_MRF_list()
		self.root.destroy()
