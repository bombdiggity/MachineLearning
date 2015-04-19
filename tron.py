# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:52:04 2015

@author: bombdiggity
"""
import matplotlib.pyplot as plt
import random
import numpy as np

class tron:
    
    def __init__(self):   
        self.dataSetCount = 0
        self.X = []
        self.W = [random.uniform(-1,1) for j in range (2)]
        self.misMatched = []
        self.iteration = 0
    
    def createDataSet(self,N):    
        self.dataSetCount = N
        
        for i in range(N):
            x = random.uniform(-1,0)
            y = random.uniform(-1,1)
            self.X.append([1,x,1])            
            plt.plot(x,y,'bo')
            
        for i in range(N):
            x = random.uniform(0,1)
            y = random.uniform(-1,1)
            self.X.append([1,x,-1])
            plt.plot(x,y,'ro')
        

    def updateWeights(self):
        
        if(self.iteration != 0):
            index = random.randint(0,len(self.misMatched)-1)
            node = self.misMatched[index]
            #print "node", node
            self.W[0] = self.W[0] + node[2]
            self.W[1] = self.W[1] + node[2] * node [1]
            
            print "W[0]", self.W[0], "W[1]", self.W[1]
            
            self.misMatched[:] = []
            
            
    def drawLine(self):
                
        ww = self.W
        if(self.iteration == 0):
            plt.plot([ww[0],-ww[0]],[-ww[1],ww[1]],'k-')
        else:
            if(len(self.misMatched) == 0):
                plt.plot([ww[0],-ww[0]],[-ww[1],ww[1]],'g--')
            else:
                "plt.plot([ww[0],-ww[0]],[-ww[1],ww[1]],'r--')"

    def trainWeights(self):
        #print "Training Weights"
        isLearned = False
        
        while isLearned == False:
            
            matchCount = 0
            mismatchCount = 0
            self.updateWeights()            
            
            for i in range(2*self.dataSetCount):
                data = self.X[i]
                res = self.W[0]*data[0] + self.W[1]*data[1]
                if(np.sign(res) == data[2]):
                    matchCount = matchCount+1
                else:
                    mismatchCount = mismatchCount+1
                    self.misMatched.append(data)
            
            self.iteration = self.iteration+1
            #print "Matched Nodes ", matchCount ,"Mismatch Nodes ", mismatchCount
            
            if(len(self.misMatched) == 0):
                isLearned = True
        
            self.drawLine()
            
        print "Iterations ", self.iteration
        return self.iteration

iterations = 0        
for i in range(1000):
    perceptron = tron()
    perceptron.createDataSet(50)
    perceptron.drawLine()
    iterations = iterations + perceptron.trainWeights()
    del perceptron

print "Total number of Iterations ", iterations
