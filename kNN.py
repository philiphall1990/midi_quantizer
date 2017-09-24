import os.path as path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import feature_extraction
import sklearn
import numpy as np
import FileIO as fIO

class doKMeans:

    def begin(self,inarray):
        inarray = self.make2d(inarray)
        for i in range(2,20):
            kd = KMeans(n_clusters=i)
            kd.fit(inarray)
        
            plt.plot(inarray)
            plt.draw()
            plt.show()
            print('\n\n\n======================================\n\n\n',sep='@')
            print(inarray)
            plt.imsave(path.abspath("C:\\Users\root\Desktop\graph-{0}".format(i)))
            fIO.FileIO().saveWork(inarray,'kmeansfit_{0}clusters'.format(i),2)
        return in_arr

    
    def make2d(self,a):
        out = [[0,0,0,0,0,0,0,0] for i in range(0,len(a)//8)]
        for i in range(0,len(a)-1):
            print(i)
            print(len(a))
            print(len(out))
            print(i//8)
            print(i%8)
            out[i//8][i%8] = a[i]
             