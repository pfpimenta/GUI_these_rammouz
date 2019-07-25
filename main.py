#!/usr/bin/python
# -*- coding: utf-8 -*-

# script to ... ? escrever algo aqui
# Pedro Foletto Pimenta, june-2019
###

#import tkinter
from tkinter import *
import matlab.engine
from window import *
#from Results_window import *

###

print("...initializing interface")
toniolo = window()


print("...starting simulation")
eng = matlab.engine.start_matlab()
eng.start_simulation(nargout=0)
eng.quit()
print("...simulation finished")

print("..recovering results (TODO) ")
#results_window = Results_window()
