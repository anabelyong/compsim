#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:57:47 2021

@author: bananabelyong
"""

import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random

class Road():
    def __init__(self, cd, rl, n):
        self.cd = float(cd)
        self.rl = rl
        self.n = n
        self.fullRoad = []
    
    def update_rules(self):
        road = np.zeros(self.rl)
        road[:int((self.cd*self.rl))] = 1
        road = list(road)
        np.random.shuffle(road)

        roadNext = road[:]
        self.fullRoad = [road[:]] 

        for t in range(0, self.n):
            for i in range(len(self.fullRoad[t]) - 1):
                if self.fullRoad[t][i] == 1:
                    if self.fullRoad[t][i+1] == 1:
                        roadNext[i] = 1
                    else:
                        roadNext[i] = 0
                        roadNext[i+1] = 1
                else:
                    if self.fullRoad[t][i-1] == 1:
                        roadNext[i] = 1
                        roadNext[i-1] = 0
                    else:
                        roadNext[i] = 0

            self.fullRoad.append(roadNext[:])
        
        return self.fullRoad
    
    def averageSpeed(self): #average speed at regular intervals 
        avgSpeed=[]
        # Determines the total number of cars  
        for n in range(len(self.fullRoad)):
            totalCars = self.fullRoad[n].count(1)
    
                    # Determines the number of moving cars
            movingCar =0
            if self.fullRoad[n].count(1) == 0:
                avgSpeed.append(0)
            elif self.fullRoad[n].count(1) == len(self.fullRoad[n]):
                avgSpeed.append(0)
            else:
                for i in range(len(self.fullRoad[n])-1):
                    if self.fullRoad[n][i] == 1:
                        if self.fullRoad[n][i+1] == 0:
                            movingCar += 1
                if self.fullRoad[n][-1] == 1 and self.fullRoad[n][0] == 0:
                    movingCar += 1
                            
                avgSpeed.append(movingCar/totalCars)
        
        print("Average Speed = " + str(avgSpeed))
        
    def averageSpeedForEachDensity(self):
        # Creates a list of car densities
        cd = np.linspace(0, 1, 11)

        # List to store SS average speeds
        avgSpeedperDensitySS = []

        for d in cd:
            
            # Create a road for every car density with random arrangements
            road = np.zeros(self.rl)
            road[:int((d*self.rl))] = 1
            road = list(road)
            np.random.shuffle(road)

            # Creates a future iteration to store values for the next iteration
            # and creates a list to store the values of the new iteration
            roadNext = road[:]
            fullRoad = [road]

            avgSpeed = [0,1]

            # Iterates for the following density until multiple average speed values are equal to one another
            n = 0
            while avgSpeed[n] != avgSpeed[n-1] and avgSpeed[n-1] != avgSpeed[n-2]:
                for i in range(len(fullRoad[n]) - 1):
                    if fullRoad[n][i] == 1:
                        if fullRoad[n][i+1] == 1:
                            roadNext[i] = 1
                        else:
                            roadNext[i] = 0
                            roadNext[i+1] = 1
                    else:
                        if fullRoad[n][i-1] == 1:
                            roadNext[i] = 1
                            roadNext[i-1] = 0
                        else:
                            roadNext[i] = 0

                fullRoad.append(roadNext[:])

                # Determines the total number of cars    
                totalCars = fullRoad[n].count(1)

                # Determines the number of moving cars
                movingCar = 0
                if fullRoad[n].count(1) == 0:
                    avgSpeed.append(0)
                elif fullRoad[n].count(1) == len(fullRoad[n]):
                    avgSpeed.append(0)
                else:
                    for i in range(len(fullRoad[n])-1):
                        if fullRoad[n][i] == 1:
                            if fullRoad[n][i+1] == 0:
                                movingCar += 1
                    if fullRoad[n][-1] == 1 and fullRoad[n][0] == 0:
                        movingCar += 1
                        
                    avgSpeed.append(movingCar/totalCars)

                n += 1

            avgSpeedperDensitySS.append(avgSpeed[-1])

        # Plots the SS average speed against car density
        # As car position is random, SS average speed may change
        plt.figure()
        plt.plot([d for d in cd], [spd for spd in avgSpeedperDensitySS], linewidth=3)
        plt.plot([d for d in cd], [spd for spd in avgSpeedperDensitySS], "bo")
        plt.xticks(np.linspace(0, 1, 11))
        plt.title("SS Average Speed of Cars against Road Density for Road Length %i" % self.rl)
        plt.xlabel("Road Density")
        plt.ylabel("SS Average Speed")

        plt.grid()
        plt.show()

    def car_position(self, time):
        plt.figure()
        ax = plt.axes()

        for j in range(self.rl):
            if self.fullRoad[time][j] == 1:
                ax.add_patch(patches.Rectangle((j, self.fullRoad[time][j]), 0.6, 0.3, color='r'))
        ax.axis("scaled")

        plt.title("Car Position at time %i" % time)
        plt.xlabel("Position on Road")

        ax.get_yaxis().set_visible(False)

        plt.xlim(0, self.rl)
        plt.ylim(0, 2)

        plt.show()


if __name__ == "__main__":
    test_road = Road(0.5, 100, 10)
    print(test_road.update_rules())
    test_road.averageSpeed()
    test_road.averageSpeedForEachDensity()
    test_road.car_position(5)
