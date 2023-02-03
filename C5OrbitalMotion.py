#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 01:48:04 2021

@author: bananabelyong
"""

from CelestialBodiesC5 import Mars, Phobosmoon
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.constants import G

class OrbitalMotion():
    def __init__(self, moonacceleration, marsacceleration):
        self.moonacceleration= moonacceleration
        self.velocity= Phobosmoon.velocity
        self.position= Phobosmoon.position
        self.marscceleration= marsacceleration
        self.velocity1= Mars.velocity
        self.position1= Mars.position
        self.iter= 5
        self.timestep= 100
    
    def moon_acceleration(self):
        force= G*((Phobosmoon.mass*Mars.mass)/((self.velocity1-self.velocity)**3)*(self.position-self.position1))
        self.moonacceleration= force/Phobosmoon.mass
        print(self.moonacceleration)
        return self.moonacceleration
    
    def mars_acceleration(self, force):
        force_Mars=G*((Phobosmoon.mass*Mars.mass)/((self.velocity-self.velocity1)**3))*(self.position1-self.position)
        self.mars_acceleration= force/ Mars.mass
        print(self.mars_acceleration)
        return self.mars_acceleration
     
    def changingstates(self): #using Euler-Cromer algorithm 
        A=self.timestep
        B=self.moonacceleration
        self.velocity=self.velocity+ B*self.timestep
        self.position=self.position+self.velocity*self.timestep
        A+=self.timestep
        
        self.patches[0].center = (self.position)
        self.patches[1].center = (self.position1)
        
        print(self.patches[0].center)
        return self.patches
    
     
    def init(self):
        #animator for initialiser 
        return self.patches 
    
    def run(self):
        fig=plt.figure()
        ax= plt.axes()
        
        self.patches=[]#appending empty list 
        self.patches1=[]
        
       # creating circles that need to be animated and added to list 
        print(self.position1) 
        print(self.position)
        
        #create planets of given radius, each at initial position and add to list 
        self.patch1=plt.Circle((self.position1), 600000, color="red", animated=False)
        self.patch2=plt.Circle((self.position), 400000, color="green", animated=False)
       
        self.patches.append(self.patch1)
        self.patches.append(self.patch2) 
        
        #add circles to axis
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])
        
        
        #set up axes
        ax.axis('scaled')
        ax.set_xlim(-10.3773*10**(6), 10.3773*10**(6))
        ax.set_ylim(- 10.3773* 10**(6), 10.3773*10**(6))
        ax.set_xlabel('orbit1')
        ax.set_ylabel('orbit2')
        
        #create animator 
        self.anim=FuncAnimation(fig, self.changingstates, init_func= self.init, frames = self.iter,  interval=20, repeat=True)
        return self.patches[0], self.patches[1]          
        
        plt.show() #show the plot 
        """
    def kineticEnergy(self):
        time = np.linspace(0, 100, 101)
        time = list(time)
            
        moonvelocityNow = self.velocity
        moonvelocityList = list([self.velocity]) # Storing inital velocity value
        
        
        for t in time:
            t = int(t)
            moonvelocityNow += moonvelocityList[t] + self.moonacceleration*self.timestep
            
            moonvelocityList.append(moonvelocityNow)
            
        print(moonvelocityList)
                
        marsvelocityNow = self.velocity
        marsvelocityList = list([self.velocity]) # Storing inital velocity value

        
        for t in time:
            t = int(t)
            marsvelocityNow += marsvelocityList[t] + self.marscceleration*self.timestep
            
            marsvelocityList.append(marsvelocityNow)
            
        print(marsvelocityList)  
    """
def main():
    test=OrbitalMotion(10, 10)
    test.run()


main()


                               
