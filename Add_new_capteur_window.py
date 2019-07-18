#!/usr/bin/python
# -*- coding: utf-8 -*-

# window to enter the parameters of a new capteur
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3
import os
import pickle
from convenience import *
import sys

class Add_new_capteur_window():
# window for entering the characteristics of a new capteur
# when the Done button is clicked, the capteur is saved in a .pickle file

	def __init__(self, parent):
		self.parent = parent

		# windows general layout
		self.init_main_layout(parent.root)

		# init central frame (where are the parameter entries)
		self.init_central_frame()
		
		# run mainloop
		#self.root.mainloop()

	def init_main_layout(self, parent_window):
		### init window:
		self.root = Toplevel(parent_window)
		self.root.title("Add new capteur") # "GUI - these Rammouz"
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
		text = "Saisissez les parametres du nouveau capteur, svp"
		self.text_lbl = Label(self.central_frame, text=text, font=self.text_font)
		self.text_lbl.grid(row=0, column=0)

		pad_frame = Frame(self.central_frame, height=30, bg="", colormap="new")
		pad_frame.grid(row=1, column=0)

		frame_for_entries = Frame(self.central_frame)
		frame_for_entries.grid(row=2, column=0)

		### capteur name
		lbl_name = Label(frame_for_entries, text="name:")
		lbl_name.grid(column=1, row=0)

		self.entry_name = Entry(frame_for_entries)
		self.entry_name.grid(column=2, row=0)

		### duree de conversion
		lbl_duree = Label(frame_for_entries, text="duree de conversion (s) ")
		lbl_duree.grid(column=1, row=1)

		self.entry_duree = Entry(frame_for_entries)
		self.entry_duree.grid(column=2, row=1)

		### transition basse consomation -> actif
		lbl_trans_basse_actif = Label(frame_for_entries, text="transition basse consomation -> actif (ms) ")
		lbl_trans_basse_actif.grid(column=1, row=2)

		self.entry_trans_basse_actif = Entry(frame_for_entries)
		self.entry_trans_basse_actif.grid(column=2, row=2)

		### transition actif -> basse consomation
		lbl_trans_actif_basse = Label(frame_for_entries, text="transition actif -> basse consomation (ms) ")
		lbl_trans_actif_basse.grid(column=1, row=3)

		self.entry_trans_actif_basse = Entry(frame_for_entries)
		self.entry_trans_actif_basse.grid(column=2, row=3)

		### consomation mode actif
		lbl_conso_actif = Label(frame_for_entries, text="consomation mode actif (uA) ")
		lbl_conso_actif.grid(column=1, row=4)

		self.entry_conso_actif = Entry(frame_for_entries)
		self.entry_conso_actif.grid(column=2, row=4)

		### consomation mode basse consomation
		lbl_conso_basse = Label(frame_for_entries, text="consomation mode basse consomation (uA) ")
		lbl_conso_basse.grid(column=1, row=5)

		self.entry_conso_basse = Entry(frame_for_entries)
		self.entry_conso_basse.grid(column=2, row=5)

	def verify_capteur_params(self, capteur_params):
		# verify if the parameters of the capteur are valid
		if(isinstance(capteur_params["name"], str) == False):
			return False
		if(is_number(capteur_params["duree"]) == False):
			return False
		if(is_number(capteur_params["trans_basse_actif"]) == False):
			return False
		if(is_number(capteur_params["trans_actif_basse"]) == False):
			return False
		if(is_number(capteur_params["conso_actif"]) == False):
			return False
		if(is_number(capteur_params["conso_basse"]) == False):
			return False
		return True # no problems

	def save_capteur(self):
		
		# put params into a dict
		capteur_params = {}
		# name :
		capteur_params["name"] =  self.entry_name.get()
		# conversion en signal electrique :
		capteur_params["duree"] =  self.entry_duree.get()
		# transitions :
		capteur_params["trans_basse_actif"] =  self.entry_trans_basse_actif.get()
		capteur_params["trans_actif_basse"] =  self.entry_trans_actif_basse.get()
		# consommation :
		capteur_params["conso_actif"] =  self.entry_conso_actif.get()
		capteur_params["conso_basse"] =  self.entry_conso_basse.get()
		#print("debug capteur_params : {}".format(capteur_params)) # DEBUG

		if(self.verify_capteur_params(capteur_params) == False):
			# parameters not valid !
			print("ERROR : capteur parameters not valid")
			#sys.exit("ERROR : capteur parameters not valid")
		else:
			# create pickle file to save capteur params
			components_folder_path = os.getcwd() + "/components/"
			capteur_filename = components_folder_path + "capteur_" + capteur_params["name"] + ".pickle"
			pickling_on = open(capteur_filename,"wb")
			pickle.dump(capteur_params, pickling_on)
			pickling_on.close()

	def cancel(self):
		self.root.destroy()

	def done(self):
		self.save_capteur()
		self.parent.update_capteur_list()
		self.root.destroy()
