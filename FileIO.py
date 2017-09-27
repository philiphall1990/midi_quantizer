from pandas.io import pickle
from os import walk, path
import os
from joblib import Parallel, delayed
import multiprocessing
from os.path import join
import PrepareForLearning as pl
import numpy as np
import kNN

class FileIO:
    """description of class"""
    def __init__(self, **kwargs):
        self.arr = []
        self.nparr = np.empty((0,8),dtype=list)
        self.inst = pl.PrepareForLearning()


    def saveWork(self, obj, quick_descr, ntries, _path="C:\\Users\\root\\Desktop\\pickle-{0}-{1}"):
        for i in range(0,ntries):
            _path = path.abspath(_path.format(quick_descr,i))
            if not path.exists(_path):
                pickle.to_pickle(obj,_path)


    def getfilefromuser(self):
        inputs = []
        curdir = os.path.join(os.path.realpath(os.curdir),"\\midi\\")
        if not os.path.exists(curdir):
            curdir = os.path.join(os.)
        for (dirpath, dirnames, filenames) in walk(os.path.join(curdir,"\\midi\\")):
            for f in [x for x in filenames if str(x).endswith("mid")]:
                #inputs.append(join(dirpath,f))
                inputs.append(join(dirpath,f))
        for p in inputs:
           self.arr = self.arr + self.inst.trackIn(p)
        #self.arr = self.arr + Parallel(-1,verbose=5)(delayed(self.inst.trackIn)(p) for p in inputs)
        self.nparr = np.asarray(self.arr,dtype=list)
        self.nparr = self.nparr.reshape(len(self.arr)//8, 8)
        self.saveWork(self.arr,'rawmidi',20)
        result = kNN.doKMeans().begin(self.arr)
        