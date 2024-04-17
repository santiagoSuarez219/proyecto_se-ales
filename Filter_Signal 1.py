# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:10:03 2021

@author: Andres_Studio
"""

#from os.path import dirname, join as pjoin
import sounddevice as sd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import signal
from scipy.fft import fft, fftfreq

#La señal fue muestreada a 192 kHz por lo que fsamp=192000

data, fsamp = sf.read('signalV.wav')
#====================================
#  Ingrese su codigo aqui




#====================================
#%%
sd.play(data, fsamp)

#Pueden reproducir la señal guardada en la variable data pero
#No escucharian señal alguna. solo cambien data por la variable
#que obtengan a la salida.