#!/usr/bin/python
# -*- coding: utf-8 -*-

# convenience functions for the GUI made for the Rammouz thesis project
# Pedro Foletto Pimenta, june-2019
###


import pickle
import os

###########################################################################
### DEFINES

DEFAULT_NUM_CAP = 1 # capteurs
DEFAULT_NUM_ADC = 1 # ADCs
DEFAULT_NUM_MSP = 1 # microprocesseurs
DEFAULT_NUM_MEM = 1 # memoires
DEFAULT_NUM_RF = 1 # modules radiofrequence

PAGE_NAMES_SCENARIO_1 = ["StartPage", "ScenariosPage", "CapteursPage", "ADCPage", "MemoryPage", "MSPPage", "MRFPage", "ProblemePage1", "ProblemePage2", "ProblemePage3", "EndPage"] # ordered


THESIS_LINK = "link to the thesis (in pdf):\n https://tel.archives-ouvertes.fr/tel-02004444/document "
START_PAGE_TEXT = "Graphic Visual Interface for the simulation of the thesis named\n\"Optimisation de la gestion d’énergie dans les systèmes embarqués\"\n\nGUI coded by Pedro FOLETTO PIMENTA"
END_PAGE_TEXT =  "Press \"Done\" to start simulation"

#remote patient monitoring
#network of wearable sensors



# fonts for the labels
font_params = 'Helvetica 11'
font_subtitles = 'Helvetica 16 bold'
font_titles = 'Helvetica 24 bold'


###########################################################################
### FUNCTIONS

def save_parameters(params):
	# TODO
	print("...saving simulation parameters")


	# pickle_off = open("Emp.pickle","rb")
	# emp = pickle.load(pickle_off)
	# print(emp)

	# put parameters in a .mat file and save it


def getCapteur(capteur_name):
	# loads the parameters of the capteur named capteur_name
	# print("DEBUG getCapteur... capteur_name : {}".format(capteur_name))

	# load pickle file to load capteur params
	components_folder_path = os.getcwd() + "/components/"
	capteur_filename = components_folder_path + "capteur_" + capteur_name + ".pickle"
	file = open(capteur_filename,"rb")
	capteur = pickle.load(file)
	file.close()

	return capteur

def getADC(ADC_name):
	# loads the parameters of the ADC named ADC_name
	# print("DEBUG getADC... ADC_name : {}".format(ADC_name))

	# load pickle file to load ADC params
	components_folder_path = os.getcwd() + "/components/"
	ADC_filename = components_folder_path + "ADC_" + ADC_name + ".pickle"
	file = open(ADC_filename,"rb")
	ADC = pickle.load(file)
	file.close()

	return ADC

def getMemory(memory_name):
	# loads the parameters of the memory named memory_name
	# print("DEBUG getMemory... memory_name : {}".format(memory_name))

	# load pickle file to load memory params
	components_folder_path = os.getcwd() + "/components/"
	memory_filename = components_folder_path + "memory_" + memory_name + ".pickle"
	file = open(memory_filename,"rb")
	memory = pickle.load(file)
	file.close()

	return memory

def getMSP(MSP_name):
	# loads the parameters of the MSP named MSP_name
	# print("DEBUG getMSP... MSP_name : {}".format(MSP_name))

	# load pickle file to load MSP params
	components_folder_path = os.getcwd() + "/components/"
	MSP_filename = components_folder_path + "MSP_" + MSP_name + ".pickle"
	file = open(MSP_filename,"rb")
	MSP = pickle.load(file)
	file.close()

	return MSP

def getMRF(MRF_name):
	# loads the parameters of the MRF named MRF_name
	#print("DEBUG getMRF... MRF_name : {}".format(MRF_name))

	# load pickle file to load MRF params
	components_folder_path = os.getcwd() + "/components/"
	MRF_filename = components_folder_path + "MRF_" + MRF_name + ".pickle"
	file = open(MRF_filename,"rb")
	MRF = pickle.load(file)
	file.close()

	return MRF



def is_number(s):
	# check if a string is a number (float)
    try:
        float(s)
        return True
    except ValueError:
        return False