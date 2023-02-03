#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:24:31 2021

@author: bananabelyong

Anabel Yong, s1911568
Mandelbrot Set

"""
import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2.025,0.6,100) #(minimum, maximum value) 
y = np.linspace(-1.125,1.125,100)
x_axis = []
y_ayis = []

class mandelbrot_set():
    def __init__(self, n):
        self.n= n
      
    def mandelbrot(self, c):
        z=0 #initial condition 
        for i in range (self.n):
            z=z**2+c #this equation would run first before checking 
            if abs(z)>2: #diverges and not in set
                return i+1
        return self.n #can be 255 of self.n 
    
    def mandel_set(self, x, y):
        data=np.zeros((len(y),len(x)))#making 2D grid with number of steps 
        for x_index, i in enumerate(x):
            for y_index, z in enumerate(y): #nested loop method for xy dimensions
            #for values within the set z<2
                c=i+z*((-1)**(1/2))
                data[y_index,x_index]= self.mandelbrot(c) #transposing x and y axis. 
        return data 
    
    
   
mandelbrot_set(255)
fred=mandelbrot_set(255)
fred.mandel_set(x, y)
#imageofMandelbrotset
plt.imshow(fred.mandel_set(x, y))
plt.show()


     

    
    
    
                    
