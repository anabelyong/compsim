#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 03:11:57 2021

@author: bananabelyong

Anabel Yong, s1911568
Checkpoint 1, Polynomial 

"""

import math 

class Polynomial(): 
    
    def __init__(self, coefficients):
        """this input is to ensure coefficient ai values are supplied as lists instead
        of tuple arguments
        
        inputs: coefficients are in same form [a_n,...,a_1, a_0]
        """
        self.coefficients = list(coefficients) 
        
    def __repr__(self):
        """this is to return the canonical string representation of the polynomial.
        """
        return "Polynomial" + str(self.coefficients)
    
    def __call__(self, x):
        result= 0 #result variable is a neutral solution which starts as 0; identity element of sum operation starts 
        #with zero.
        for index, coeff in enumerate(self.coefficients): #
            result += coeff*(x** index)
        return result
    
    def polyprint(self):
        function= str(self.coefficients[0])
        
        for num in range(1, len(self.coefficients)):
            if self.coefficients[num]==0:
                continue
            elif self.coefficients[num] < 0:
                if num ==1:
                    function+=" - " + str(self.coefficients[num]) + "x"
                
                elif self.coefficients[num]==-1:
                    function+=" - " + "x^" + str(num)
                else:
                    function+=" - " + str(self.coefficients[num]) + "x^" + str(num)
            elif self.coefficients[num] > 0:
                if self.coefficients[num]==1:
                    function+= " + " + "x" + str(num)
                else:
                    function+= " + " +  str(self.coefficients[num]) +  "x^" + str(num)
                    
        return function
        
    def order(self):
            return len(self.coefficients)-1

    def add(self, poly):
        newcoefficients=[]
        if len(self.coefficients)< len(poly.coefficients):
             for index, coeff in enumerate(poly.coefficients): 
                 newcoefficients.append(self.coefficients[index] + poly.coefficients[index])
             for index in range(len(self.coefficients), len(poly.coefficients)):
                 newcoefficients.append(poly.coefficients[index])
                                       
        elif len(self.coefficients)== len(poly.coefficients):
             for index, coeff in enumerate(poly.coefficients): 
                 newcoefficients.append(self.coefficients[index] + poly.coefficients[index])
        
        else:
             for index, coeff in enumerate(poly.coefficients): 
                 newcoefficients.append(self.coefficients[index] + poly.coefficients[index])
             for index in range(len(poly.coefficients), len(self.coefficients)):
                 newcoefficients.append(self.coefficients[index])
            
        return Polynomial(newcoefficients)
        
    def differentiation(self):
        result=[]
        for index, coeff in enumerate(self.coefficients):
            result.append(index*self.coefficients[index])
        return Polynomial(result[1:])
    
    def integrate(self,c):
        result=[c]
        for index, coeff in enumerate(self.coefficients):
            result.append((self.coefficients[index])/(index+1))
        return Polynomial(result)

def main():
    pa=Polynomial([2,0,4,-1,0,6])
    pb=Polynomial([-1,-3,0, 4.5])
    
    pc=pa.differentiation()
    print(pc.integrate(2))
     
main()
    
        
        
            

    

            
    
    
