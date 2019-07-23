#!/usr/bin/python
# -*- coding: utf-8 -*-

# convenience functions for the GUI made for the Rammouz thesis project
# Pedro Foletto Pimenta, june-2019
###


import pickle
import os
import scipy.io as sio


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

def get_capteur_init(capteur_params):
	# returns an array with 5 places for the parameters of the capteur
	capteur_init = [capteur_params["duree"],
			capteur_params["trans_basse_actif"],
			capteur_params["trans_actif_basse"],
			capteur_params["conso_actif"],
			capteur_params["conso_basse"]
		]
	# garantee that they are all floats
	capteur_init = [float(x) for x in capteur_init]
	
	return capteur_init

def get_adc_init(adc_params):
	# returns an array with 6 places for the parameters of the adc
	adc_init = [adc_params["temps"],
			adc_params["trans_basse_actif"],
			adc_params["trans_actif_basse"],
			adc_params["conso_actif"],
			adc_params["conso_basse"],
			adc_params["conso_conversion"]
		]
	# garantee that they are all floats
	adc_init = [float(x) for x in adc_init]
	
	return adc_init

def get_memoire_init(memory_params):
	# returns an array with 19 places for the parameters of the memory
	memoire_init = [memory_params["taille"],
			memory_params["octets_instruction"],
			memory_params["freq_spi"],
			memory_params["octets_ecriture"],
			memory_params["duree_ecriture"],
			memory_params["octets_lecture"],
			memory_params["duree_lecture"],
			memory_params["octets_effacement"],
			memory_params["duree_effacement"],
			memory_params["trans_basse1_actif"],
			memory_params["trans_actif_basse1"],
			memory_params["trans_basse2_actif"],
			memory_params["trans_actif_basse2"],
			memory_params["conso_actif"],
			memory_params["conso_ecriture"],
			memory_params["conso_lecture"],
			memory_params["conso_effacement"],
			memory_params["conso_basse1"],
			memory_params["conso_basse2"]
		]
	# garantee that they are all floats
	memoire_init = [float(x) for x in memoire_init]
	
	return memoire_init

def get_processeur_init(processeur_params):
	# returns an array with 15 places for the parameters of the processeur
	processeur_init = [processeur_params["trans_basse1_actif"],
			processeur_params["trans_actif_basse1"],
			processeur_params["trans_basse2_actif"],
			processeur_params["trans_actif_basse2"],
			processeur_params["conso_actif_1"],
			processeur_params["conso_actif_4"],
			processeur_params["conso_actif_8"],
			processeur_params["conso_actif_12"],
			processeur_params["conso_actif_16"],
			processeur_params["conso_basse1_1"],
			processeur_params["conso_basse1_4"],
			processeur_params["conso_basse1_8"],
			processeur_params["conso_basse1_12"],
			processeur_params["conso_basse1_16"],
			processeur_params["conso_basse2"]
		]
	# garantee that they are all floats
	processeur_init = [float(x) for x in processeur_init]
	
	return processeur_init

def get_module_rf_init(module_rf_params):
	# returns an array with 13 places for the parameters of the module_rf
	module_rf_init = [module_rf_params["connection_interval"],
			module_rf_params["advertising_interval"],
			module_rf_params["trans_basse1_actif"],
			module_rf_params["trans_actif_basse1"],
			module_rf_params["trans_basse2_actif"],
			module_rf_params["trans_actif_basse2"],
			module_rf_params["transm_1"],
			module_rf_params["transm_7"],
			module_rf_params["transm_15"],
			module_rf_params["conso_reception"],
			module_rf_params["conso_actif"],
			module_rf_params["conso_basse1"],
			module_rf_params["conso_basse2"]
		]
	# garantee that they are all floats
	module_rf_init = [float(x) for x in module_rf_init]
	
	return module_rf_init

def save_parameters(params):
	# TODO
	# put parameters in a simulation_params.mat file and save it
	print("...saving simulation parameters")

	# dict to be saved in the .mat file
	simulation_params = {}
	simulation_params["nb_composant"] = [1, 1, 1, 1, 1] # TODO
	# Capacité de la source : variable
	simulation_params["capacite_batterie"] = []
	simulation_params["periode_mesure"] = int(params["Probleme"]["periode_mesure"])

	# SOLUTION TEMPORAIRE : alg_connexion == "continu toujours"
	simulation_params["periode_transmission"] = int(params["Probleme"]["periode_mesure"])
	# if(params["Probleme"]["alg_connexion"] == "continu"):
	# 	simulation_params["periode_transmission"] = int(params["Probleme"]["periode_mesure"])
	# else: # "syncronise"
	# 	simulation_params["periode_transmission"] = # get value from a new entry # TODO
	
	simulation_params["frequence_cpu"] = int(params["Probleme"]["freq_traitement"])
	simulation_params["puissance_rf_tx"] = int(params["Probleme"]["puissance_transmission"])
	simulation_params["adc_nb_echantillons"] = int(params["Probleme"]["freq_echantillonage"])
	simulation_params["routine"] = params["Probleme"]["routine"] # ["predefini", "aleatoire", "non connu"]
	# Autonomie du noeud : variable
	simulation_params["autonomie"] = []
	simulation_params["p_sup_processeur"] = [1, 4, 8, 12, 16]
	simulation_params["p_sup_module_rf"] = [1, 7, 15]
	simulation_params["capteur_init"] = get_capteur_init(params["capteur"])
	simulation_params["adc_init"] = get_adc_init(params["ADC"])
	simulation_params["memoire_init"] = get_memoire_init(params["memory"])
	simulation_params["processeur_init"] = get_processeur_init(params["MSP"])
	simulation_params["module_rf_init"] = get_module_rf_init(params["MRF"])
	simulation_params["n_jours"] = float(params["Probleme"]["duree_monitoring"])

	sio.savemat(os.getcwd() + '/simulation_params.mat', simulation_params)

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