import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot


class BuildRegression:
    def __init__(self , X , y ,T , features , callback):
        self.X = X
        self.y = y
        self.T = T
        self.callback = callback
        self.features = features
        self.coefficients = [ 0 for i in range(features+1) ]
        plt.ion()
        
    @staticmethod
    def f(x,a,b):
        return a*x + b
        
    @staticmethod
    def draw_line(func , a , b):
        x = np.arange(-3.5, 3.5, 0.1)
        y = func(x , a , b)
        line = pyplot.plot(x,y , color = "r")
        return line    
        
    def getSampleRegression(self):
        features = self.features
        X = self.X 
        y = self.y
        learning_rate = 0.2
        coefficients = self.coefficients
        while self.is_All_derives_zero() is False:
            self.run_Gradient_descendent (learning_rate)
            if self.features == 1:
                self.callback(coefficients , self.features , self.T , y )
        return coefficients    
        
    
    @staticmethod
    def hTetha( Xsample , coefficients):
        value = 0
        for i in range(len(Xsample)):
            value += Xsample[i]*coefficients[i]
        return value



    def costFunction( self):
        X = self.X 
        y = self.y 
        coefficients = self.coefficients
        cost = 0
        for i in range(len(X)):
            cost += (BuildRegression.hTetha(X[i] , coefficients) - y[i]) * (BuildRegression.hTetha(X[i] , coefficients) - y[i])
        return cost/(2*len(X))
        
        
    def derivate_to_tethaJ( self , j ):
        X = self.X
        y = self.y
        coefficients = self.coefficients
        deriv = 0
        for i in range(len(X)):
            deriv += (BuildRegression.hTetha(X[i] , coefficients) - y[i]) * X[i][j]      
        return deriv / len(X)
        
    def is_All_derives_zero(self):
        X = self.X
        y = self.y
        coefficients = self.coefficients
        for i in range(len(coefficients)):
            if abs(self.derivate_to_tethaJ(i)) > 0.00000001:
                return False
        return True
        
    def run_Gradient_descendent( self , learning_rate):
        X = self.X
        y = self.y 
        coefficients = self.coefficients
        for i in range(len(coefficients)):
            coefficients[i] -= learning_rate * self.derivate_to_tethaJ(i)
            