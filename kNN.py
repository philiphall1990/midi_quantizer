import os.path as path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import sklearn
import numpy as np
import FileIO as fIO

class doKMeans:

    def begin(self,inarray):
        inarray = np.reshape(inarray, (len(inarray),1))
        inarray = np.resize(inarray,(len(inarray//8),8))
        inarray = normalize(inarray)
        for i in range(2,20):
            kd = KMeans(n_clusters=i)
            temparray = inarray
            result = kd.fit_transform(temparray)
            params = kd.get_params()
            print('\n\n\n======================================\n\n\n',sep='@')
            print(result)
            print(params)
            
            
            
            fIO.FileIO().saveWork((result,params),'kmeansfit_{0}clusters'.format(i),2)
        input("press any key to exit...")