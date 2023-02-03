#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:20:26 2021

@author: bananabelyong

Anabel Yong, s1911568

Checkpoint 2, Radioactive Decay 

"""
import matplotlib.pyplot as plt 
import numpy as np
import random 
from scipy.integrate import odeint
    
t_half_iodine= 24.98 #initial conditions 
t1           = 100
p_decay_iodine= 0.02775
lengthof2DarrayN =  int(input("Give 'N' value: "))
timestep=float(input("Give 'timestep' value: "))

numbercount= lengthof2DarrayN * lengthof2DarrayN #mutiplies 50 X 50 

print(p_decay_iodine)

def analytic(lengthof2DarrayN, timestep):
    '''Analytic solution for the iodine-128 count'''
    return lengthof2DarrayN * np.exp (-timebase/t_half_iodine * np.log(2))

def simulate_monte_carlo(lengthof2DarrayNlengthof2DarrayN, t1, timestep, numbercount):
    '''Monte carlo simulation for iodine-128 counts'''
    dt             = t1 / timestep #Calculating the interval between each time division
    count_iodine   = np.zeros((lengthof2DarrayN)) #creating zero arrays to put the counts into
    atoms          = np.ones((lengthof2DarrayN,lengthof2DarrayN)) #Creating an array of numbers to represent the atoms in the simulation
    time=0
    
    while numbercount > ((lengthof2DarrayN)**2)/2:
        for x128 in range(lengthof2DarrayN):
            for y128 in range(lengthof2DarrayN):
                if atoms[x128,y128] ==0: #Deciding whether the given atom should decay
                    if random.random() <= p_decay_iodine:
                        atoms[x128,y128] = 1 #lattice is either 0 (decayed nuclei) or 1 (undecayed)
                        numbercount-=1
                    else:
                        atoms[x128,y128] = 0 #undecayed
        time+= timestep #adds 0.01 to the time, to keep count of decay.
        
timebase= np.arange(0, t1, t1/timestep) #creating the array of times for use in the analytic solution and scipy
n_analytic = analytic(lengthof2DarrayN,  timestep) #Calling the analytic solution
n_iodine= simulate_monte_carlo(lengthof2DarrayN, t1, timestep, numbercount) #Calling the Monte Carlo Simulation   

print(n_iodine)

def f(N, t):
    '''Differential for the decay, for use with odeint'''
    N_iodine = lengthof2DarraysN #unpacking N
    tau_iodine = t_half_iodine / np.log(2)
    DEQ_iodine = - lengthof2DarraysN/ tau_iodine
    
    return np.array((DEQ_iodine)) #repacking



N0_iodine= 250 #Initial conditions for scipy
lengthof2DarrayN = np.array((n_iodine))
n_scipy = odeint(f, N0, timestep) #Calling scipy odeint



