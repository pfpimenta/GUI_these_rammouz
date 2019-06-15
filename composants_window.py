#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *

DEFAULT_NUM_CAP = 1 # capteurs
DEFAULT_NUM_ADC = 1 # ADCs
DEFAULT_NUM_MSP = 1 # microprocesseurs
DEFAULT_NUM_MEM = 1 # memoires
DEFAULT_NUM_RF = 1 # modules radiofrequence


# dict with parameters
params = {}
params['numCapteurs'] = 0
params['numADCs'] = 0
params['numMicroprocesseurs'] = 0
params['numMemoires'] = 0
params['numModulesRadiofrequence'] = 0




class Composants_window():
# 

	def __init__(self):
		self.root = Tk()

		lbl = Label(self.root, text="Feuille Simulation")
		lbl.grid(column=0, row=0)

		### NUM CAPTEURS

		lbl_numCapteurs = Label(self.root, text="num. de Capteurs:")
		lbl_numCapteurs.grid(column=1, row=1)

		s_numCapteurs = StringVar()
		self.entry_numCapteurs = Entry(self.root, textvariable=s_numCapteurs)
		self.entry_numCapteurs.grid(column=2, row=1)
		s_numCapteurs.set(str(DEFAULT_NUM_CAP))
		#self.entry_numCapteurs.set("1") # default value

		### NUM ADCs

		lbl_numADCs = Label(self.root, text="num. de ADCs:")
		lbl_numADCs.grid(column=1, row=2)

		s_numADCs = StringVar()
		self.entry_numADCs = Entry(self.root, textvariable=s_numADCs)
		self.entry_numADCs.grid(column=2, row=2)
		s_numADCs.set(str(DEFAULT_NUM_ADC))

		### NUM microprocesseurs

		lbl_numMSPs = Label(self.root, text="num. de microprocesseurs:")
		lbl_numMSPs.grid(column=1, row=3)

		s_numMSPs = StringVar()
		self.entry_numMSPs = Entry(self.root, textvariable=s_numMSPs)
		self.entry_numMSPs.grid(column=2, row=3)
		s_numMSPs.set(str(DEFAULT_NUM_MSP))

		### NUM memoires

		lbl_numADCs = Label(self.root, text="num. de memoires:")
		lbl_numADCs.grid(column=1, row=4)

		s_numMems = StringVar()
		self.entry_numMems = Entry(self.root, textvariable=s_numMems)
		self.entry_numMems.grid(column=2, row=4)
		s_numMems.set(str(DEFAULT_NUM_MEM))

		### NUM modules radiofrequence

		lbl_numRFs = Label(self.root, text="num. de modules radiofrequence:")
		lbl_numRFs.grid(column=1, row=5)

		s_numRFs = StringVar()
		self.entry_numRFs = Entry(self.root, textvariable=s_numRFs)
		self.entry_numRFs.grid(column=2, row=5)
		s_numRFs.set(str(DEFAULT_NUM_RF))


		print_button = Button(self.root, text = 'Print', command=self.print_entries)
		print_button.grid(column=6, row=6)

		next_button = Button(self.root, text = 'Next', command=self.next_page)
		next_button.grid(column=7, row=7)

		self.root.mainloop()

	def print_entries(self):
		print(self.entry_numCapteurs.get())
		print(self.entry_numADCs.get())

	def next_page(self):
		self.root.destroy()
		

	def quit(self):
		self.root.destroy()