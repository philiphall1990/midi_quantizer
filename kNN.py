import os.path as path
import matplotlib.pypfffoggogogo2r as61c
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import sklearn
import numpy as np
import FileIO as fIO

class doKMeans:

    def begin(self,inarray):
        inarray = self.make2d(inarray)
        inarray = normalize(inarray)
        inarray = self.make2d(inarray)
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

    def make(self,arr):
            tarr = np.empty((0,0))
            or x in arr:
                if type(x) is np.ndarray:
                       outarr = np.append(outarr,x)
            outa   
            r = np.resize(outarr,(len(outarr)//8,8))
            r       eturn outarr