import os.path as path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import feature_extraction
import sklearn
import numpy as np
import FileIO as fIO

class doKMeans:

    def begin(self,inarray):
        inarray = np.copy(inarray)
        for i in range(2,20):
            kd = KMeans(n_clusters=i)
            inarray = np.resize(inarray,(len(inarray//8),8))
            kd.fit(inarray)
        
            print('\n\n\n======================================\n\n\n',sep='@')
            print(inarray)
           
            fIO.FileIO().saveWork(inarray,'kmeansfit_{0}clusters'.format(i),2)