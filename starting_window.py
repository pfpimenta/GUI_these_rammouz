#!/usr/bin/python
# -*- coding: utf-8 -*-

# ??????????
# Pedro Foletto Pimenta, june-2019
###
from tkinter import *



class Starting_window():

	def __init__(self):
		self.root = Tk()
		self.root.title("NOME DO PROGRAMA? tem q ver dps") # "GUI - these Rammouz"
		#self.root.geometry('800x600')
		#self.root.configure(background="black")


		corner_frame = Frame(width=40, height=20, bg="", colormap="new")
		corner_frame.grid(column=0, row=0)

		central_frame = Frame(width=500, height=500, bg="", colormap="new")
		central_frame.grid(column=1, row=1)

		#central_text = "Type the parameters\nand then click \"Done\"\nto start the simulation")
		#central_text = "\t\t\t\t\t\t\t\t\t\nfait par Pedro FOLETTO PIMENTA"
		central_text = "GUI pour la simulation de simulation de la consommation\nd'energie pour la conception des reseaux de capteurs biomedicaux.\n[description ici?]\n\n\nfait par Pedro FOLETTO PIMENTA (2019)"
		lbl = Label(central_frame, text=central_text)
		lbl.pack()


		next_button = Button(self.root, text = 'Next', command=self.quit)
		next_button.grid(column=7, row=7, sticky=E)
		corner_frame_2 = Frame(width=40, height=20, bg="", colormap="new")
		corner_frame_2.grid(column=8, row=8)
		
		self.root.mainloop()

	def quit(self):
		self.root.destroy()