#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *


class Probleme_window():
# 

	def __init__(self):
		self.root = Tk()

		lbl = Label(self.root, text="Feuille Probleme")
		lbl.grid(column=0, row=0)

		lbl_numCapteurs = Label(self.root, text="num. de Capteurs:")
		lbl.grid(column=0, row=1)

		entry_numCapteurs = Entry(self.root)
		entry_numCapteurs.grid(column=1, row=1)

		next_button = Button(self.root, text = 'Next', command=self.quit)
		next_button.grid(column=7, row=7)

		self.root.mainloop()

	def quit(self):
		self.root.destroy()
