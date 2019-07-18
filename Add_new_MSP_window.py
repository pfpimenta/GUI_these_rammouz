#!/usr/bin/python
# -*- coding: utf-8 -*-

# window to enter the parameters of a new MSP (microprocesseur)
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
import os
import pickle
from convenience import *
import sys

class Add_new_MSP_window():
# window for entering the characteristics of a new MSP (microprocesseur)
# when the Done button is clicked, the MSP is saved in a .pickle file

	def __init__(self, parent):
		self.parent = parent

		# windows general layout
		self.init_main_layout(parent.root)

		# init central frame (where are the parameter entries)
		self.init_central_frame()
		
	def init_main_layout(self, parent_window):
		### init window:
		self.root = Toplevel(parent_window)
		self.root.title("Add new MSP") # "GUI - these Rammouz"
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

		### MSP name
		lbl_name = Label(frame_for_entries, text="name: ")
		lbl_name.grid(column=1, row=current_row)

		self.entry_name = Entry(frame_for_entries)
		self.entry_name.grid(column=2, row=current_row)
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

		### Consommation actif (frequence de traitement == 1 MHz)
		lbl_conso_actif_1 = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif_1.grid(column=1, row=current_row)

		self.entry_conso_actif_1 = Entry(frame_for_entries)
		self.entry_conso_actif_1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Consommation actif (frequence de traitement == 4 MHz)
		lbl_conso_actif_4 = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif_4.grid(column=1, row=current_row)

		self.entry_conso_actif_4 = Entry(frame_for_entries)
		self.entry_conso_actif_4.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Consommation actif (frequence de traitement == 8 MHz)
		lbl_conso_actif_8 = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif_8.grid(column=1, row=current_row)

		self.entry_conso_actif_8 = Entry(frame_for_entries)
		self.entry_conso_actif_8.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Consommation actif (frequence de traitement == 12 MHz)
		lbl_conso_actif_12 = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif_12.grid(column=1, row=current_row)

		self.entry_conso_actif_12 = Entry(frame_for_entries)
		self.entry_conso_actif_12.grid(column=2, row=current_row)
		current_row = current_row + 1

		### Consommation actif (frequence de traitement == 16 MHz)
		lbl_conso_actif_16 = Label(frame_for_entries, text="consomation mode actif (mA) ")
		lbl_conso_actif_16.grid(column=1, row=current_row)

		self.entry_conso_actif_16 = Entry(frame_for_entries)
		self.entry_conso_actif_16.grid(column=2, row=current_row)
		current_row = current_row + 1
		
		### consomation mode basse consomation 1 (frequence de traitement == 1 MHz)
		lbl_conso_basse1_1 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1_1.grid(column=1, row=current_row)

		self.entry_conso_basse1_1 = Entry(frame_for_entries)
		self.entry_conso_basse1_1.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 1 (frequence de traitement == 4 MHz)
		lbl_conso_basse1_4 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1_4.grid(column=1, row=current_row)

		self.entry_conso_basse1_4 = Entry(frame_for_entries)
		self.entry_conso_basse1_4.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 1 (frequence de traitement == 8 MHz)
		lbl_conso_basse1_8 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1_8.grid(column=1, row=current_row)

		self.entry_conso_basse1_8 = Entry(frame_for_entries)
		self.entry_conso_basse1_8.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 1 (frequence de traitement == 12 MHz)
		lbl_conso_basse1_12 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1_12.grid(column=1, row=current_row)

		self.entry_conso_basse1_12 = Entry(frame_for_entries)
		self.entry_conso_basse1_12.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 1 (frequence de traitement == 16 MHz)
		lbl_conso_basse1_16 = Label(frame_for_entries, text="consomation mode basse consomation 1 (uA) ")
		lbl_conso_basse1_16.grid(column=1, row=current_row)

		self.entry_conso_basse1_16 = Entry(frame_for_entries)
		self.entry_conso_basse1_16.grid(column=2, row=current_row)
		current_row = current_row + 1

		### consomation mode basse consomation 2
		lbl_conso_basse2 = Label(frame_for_entries, text="consomation mode basse consomation 2 (uA) ")
		lbl_conso_basse2.grid(column=1, row=current_row)

		self.entry_conso_basse2 = Entry(frame_for_entries)
		self.entry_conso_basse2.grid(column=2, row=current_row)
		current_row = current_row + 1


	def verify_MSP_params(self, MSP_params):
		# verify if the parameters of the MSP are valid
		if(isinstance(MSP_params["name"], str) == False):
			return False
		if(is_number(MSP_params["trans_basse1_actif"]) == False):
			return False
		if(is_number(MSP_params["trans_actif_basse1"]) == False):
			return False
		if(is_number(MSP_params["trans_basse2_actif"]) == False):
			return False
		if(is_number(MSP_params["trans_actif_basse2"]) == False):
			return False
		if(is_number(MSP_params["conso_actif_1"]) == False):
			return False
		if(is_number(MSP_params["conso_actif_4"]) == False):
			return False
		if(is_number(MSP_params["conso_actif_8"]) == False):
			return False
		if(is_number(MSP_params["conso_actif_12"]) == False):
			return False
		if(is_number(MSP_params["conso_actif_16"]) == False):
			return False
		if(is_number(MSP_params["conso_basse1_1"]) == False):
			return False
		if(is_number(MSP_params["conso_basse1_4"]) == False):
			return False
		if(is_number(MSP_params["conso_basse1_8"]) == False):
			return False
		if(is_number(MSP_params["conso_basse1_12"]) == False):
			return False
		if(is_number(MSP_params["conso_basse1_16"]) == False):
			return False
		if(is_number(MSP_params["conso_basse2"]) == False):
			return False
		return True # no problems

	def save_MSP(self):
		
		# put params into a dict
		MSP_params = {}
		# name :
		MSP_params["name"] =  self.entry_name.get()
		# transitions :
		MSP_params["trans_basse1_actif"] =  self.entry_trans_basse1_actif.get()
		MSP_params["trans_actif_basse1"] =  self.entry_trans_actif_basse1.get()
		MSP_params["trans_basse2_actif"] =  self.entry_trans_basse2_actif.get()
		MSP_params["trans_actif_basse2"] =  self.entry_trans_actif_basse2.get()
		# consommation :
		MSP_params["conso_actif_1"] =  self.entry_conso_actif_1.get()
		MSP_params["conso_actif_4"] =  self.entry_conso_actif_4.get()
		MSP_params["conso_actif_8"] =  self.entry_conso_actif_8.get()
		MSP_params["conso_actif_12"] =  self.entry_conso_actif_12.get()
		MSP_params["conso_actif_16"] =  self.entry_conso_actif_16.get()
		MSP_params["conso_basse1_1"] =  self.entry_conso_basse1_1.get()
		MSP_params["conso_basse1_4"] =  self.entry_conso_basse1_4.get()
		MSP_params["conso_basse1_8"] =  self.entry_conso_basse1_8.get()
		MSP_params["conso_basse1_12"] =  self.entry_conso_basse1_12.get()
		MSP_params["conso_basse1_16"] =  self.entry_conso_basse1_16.get()
		MSP_params["conso_basse2"] =  self.entry_conso_basse2.get()
		#print("debug MSP_params : {}".format(MSP_params)) # DEBUG

		if(self.verify_MSP_params(MSP_params) == False):
			# parameters not valid !
			print("ERROR : MSP parameters not valid")
			#sys.exit("ERROR : MSP parameters not valid")
		else:
			# create pickle file to save MSP params
			components_folder_path = os.getcwd() + "/components/"
			MSP_filename = components_folder_path + "MSP_" + MSP_params["name"] + ".pickle"
			pickling_on = open(MSP_filename,"wb")
			pickle.dump(MSP_params, pickling_on)
			pickling_on.close()

	def cancel(self):
		self.root.destroy()

	def done(self):
		self.save_MSP()
		self.parent.update_MSP_list()
		self.root.destroy()
