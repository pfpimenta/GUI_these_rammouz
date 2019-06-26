#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *
from tkinter import font  as tkfont # python 3


class Add_new_capteur_window():
# 

	def __init__(self):
		# windows general layout
		self.init_main_layout()

		# init central frame (where are the parameter entries)
		self.init_central_frame()
		
		# run mainloop
		self.root.mainloop()

	def init_main_layout(self):
		### init window:
		self.root = Tk()
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

		### duree de conversion
		lbl_duree = Label(frame_for_entries, text="duree de conversion:")
		lbl_duree.grid(column=1, row=1)

		s_duree = StringVar()
		self.entry_duree = Entry(frame_for_entries, textvariable=s_duree)
		self.entry_duree.grid(column=2, row=1)
		s_duree.set("huehuehue")

		### transition basse consomation -> actif
		lbl_trans_basse_actif = Label(frame_for_entries, text="transition basse consomation -> actif:")
		lbl_trans_basse_actif.grid(column=1, row=2)

		s_trans_basse_actif = StringVar()
		self.entry_trans_basse_actif = Entry(frame_for_entries, textvariable=s_trans_basse_actif)
		self.entry_trans_basse_actif.grid(column=2, row=2)
		s_trans_basse_actif.set("sagagadga")

	def save_capteur(self):
		pass # TODO

	def cancel(self):
		self.root.destroy()

	def done(self):
		self.save_capteur()		
		self.root.destroy()
