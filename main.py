from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from matplotlib import pyplot
from dataset import dataset
import numpy as np
import math
import copy
from utility import Utility
from build_regression import BuildRegression
from draw_plot import drawPlot


class Main:
    @staticmethod
    def callback(coff , features , T , y ):
        drawPlot.draw(coff , features , T , y, fig)
if __name__ == '__main__':    
    print(" please enter number of feautures first")
    features = int(input())
    if features == 1:
        fig = plt.figure()
    datas = dataset.getData(features)
    X = datas[0]
    T = copy.deepcopy(datas[0])
    y = datas[1]
    X = Utility.insert_one_to_list(X)    
    reg = BuildRegression(X , y , T , features , Main.callback)
    final_coff = reg.getSampleRegression()
    print(final_coff)
    
