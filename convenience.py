#!/usr/bin/python
# -*- coding: utf-8 -*-

# convenience functions for the GUI made for the Rammouz thesis project
# Pedro Foletto Pimenta, june-2019
###


###########################################################################
### DEFINES

DEFAULT_NUM_CAP = 1 # capteurs
DEFAULT_NUM_ADC = 1 # ADCs
DEFAULT_NUM_MSP = 1 # microprocesseurs
DEFAULT_NUM_MEM = 1 # memoires
DEFAULT_NUM_RF = 1 # modules radiofrequence


THESIS_LINK = "https://tel.archives-ouvertes.fr/tel-02004444/document"
START_PAGE_TEXT = "Graphic Visual Interface for the simulation of the thesis named\n\"Optimisation de la gestion d’énergie dans les systèmes embarqués\"\n\nGUI coded by Pedro FOLETTO PIMENTA"
END_PAGE_TEXT =  "Press \"Done\" to start simulation"

#remote patient monitoring
#network of wearable sensors



###########################################################################
### FUNCTIONS

def save_parameters(params):
	# TODO
	print("...saving simulation parameters")


	# pickle_off = open("Emp.pickle","rb")
	# emp = pickle.load(pickle_off)
	# print(emp)

	# put parameters in a .mat file and save it


def is_number(s):
	# check if a string is a number (float)
    try:
        float(s)
        return True
    except ValueError:
        return False