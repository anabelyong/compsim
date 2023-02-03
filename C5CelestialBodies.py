#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:22:13 2021

@author: bananabelyong
"""

import math 
import matplotlib.pyplot as plt 
from scipy.constants import G
import numpy as np

#G= 6.674e-11 #gravitational constant laws

class CelestialBodies():
    def __init__(self,mass, orbital_radius, velocity, position):
        self.mass=mass
        self.orbital_radius=orbital_radius
        self.velocity=np.array(velocity)
        self.position=np.array(position)
        
Mars= CelestialBodies(6.39E23, 0, (0,0), (0,0))
Phobosmoon= CelestialBodies(1.06*10**(16), 9.3773*10**(6), (0, math.sqrt((G*Mars.mass)/ 9.3773*10**(6))), (9.3773*10**(6),1E6))
                

        

        
    
    
    

        
