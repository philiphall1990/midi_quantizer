import os.path as path
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import sklearn
import numpy as np
import FileIO as fIO

class doKMeans:

    def begin(self,inarray):
        #inarray = self.make2d(inarray)
        #inarray = normalize(inarray)
        #inarray = self.make2d(inarray)
        i = 8
        kd = KMeans(n_clusters=i)
        temparray = inarray
        result = kd.fit_transform(temparray)
        params = kd.get_params()
        print('\n\n\n======================================\n\n\n')
        print(result)
        print(params)
            
            
            
        fIO.FileIO().saveWork((result,params,kd),'kmeansfit_fulldata'.format(i),2)
        input("press any key to exit...")

    def make2d(self,arr):
        outarr = np.empty((0,0))
        for x in arr:
            if type(x) is np.ndarray:
                outarr = np.append(outarr,x)
        outarr = np.resize(outarr,(len(outarr)//8,8))
        return outarr