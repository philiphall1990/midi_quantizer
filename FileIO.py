from pandas.io import pickle
from pandas import read_pickle
from os import walk, path
import os
from joblib import Parallel, delayed
import multiprocessing
import PrepareForLearning as pl
import numpy as np
import kNN

class FileIO:
    _PATH = "C:\\Users\\root\\Desktop\\pickle-{0}-{1}"
    """description of class"""
    def __init__(self, **kwargs):
        
        self.arr = np.empty((0,0))
        self.inst = pl.PrepareForLearning()


    def saveWork(self, obj, quick_descr, ntries, _path=_PATH):
        for i in range(0,ntries):
            _path = path.abspath(_path.format(quick_descr,i))
            if not path.exists(_path):
                pickle.to_pickle(obj,_path)


    def getfilefromuser(self):
        inputs = []
        #try:
        #    self.arr = read_pickle(FileIO._PATH.format('rawmidi',0))
        #except: 
        #    print("no pickle file...will encode midi from files")
        if len(self.arr) == 0:
            curdir = os.path.abspath(os.path.join(os.path.realpath(os.curdir),"\\midi\\"))
            if not os.path.exists(curdir):
                curdir = os.path.abspath("C:\\Users\\root\\Source\\Repos\\midi_quantizer\\midi")
            for (dirpath, dirnames, filenames) in walk(curdir):
                for f in [x for x in filenames if str(x).endswith("mid")]:
                    #inputs.append(join(dirpath,f))
                    inputs.append(os.path.join(dirpath,f))
            for p in inputs:
                self.arr = np.append(self.arr, self.inst.trackIn(p))
            #self.arr = np.add(self.arr,Parallel(-1,verbose=5)(delayed(self.inst.trackIn)(p) for p in inputs))
            #self.saveWork(self.arr,'rawmidi',20)
        
        temparr = self.arr
        print("original values:\n\n\n\n\n")
        print(np.resize(temparr,(len(temparr)//8,8)))
        result = kNN.doKMeans().begin(self.arr)
        