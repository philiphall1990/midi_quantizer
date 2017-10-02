from pandas.io import pickle
from pandas import read_pickle
from os import walk, path
import os
from joblib import Parallel, delayed
import multiprocessing
import PrepareForLearning
import numpy as np
import kNN

class FileIO:
    _PATH = "C:\\pickle-{0}-{1}"
    """description of class"""
    def __init__(self, **kwargs):
        self.inst = None

    def saveWork(self, obj, quick_descr, ntries, _path=_PATH):
        for i in range(0,ntries):
            _path = path.abspath(FileIO._PATH.format(quick_descr,i))
            if not path.exists(_path):
                pickle.to_pickle(obj,_path)
                return None

    def loadWork(self, descr,_path):
        fns = os.listdir(os.path.dirname(_path))
        refobj = []
        for f in fns:
            if descr in str(f):
                refobj.append(read_pickle(os.path.join(os.path.dirname(_path),f)))
        return refobj
  

    def getfilefromuser(self):
        self.inst = PrepareForLearning.PrepareForLearning()
        inputs = []
        curdir = os.path.abspath(os.path.join(os.path.realpath(os.curdir),"\\midi\\"))
        if not os.path.exists(curdir):
            curdir = os.path.abspath("C:\\Users\\root\\Source\\Repos\\midi_quantizer\\midiFiles")
        for (dirpath, dirnames, filenames) in walk(curdir):
            for f in [x for x in filenames if str(x).endswith("mid")]:
                #inputs.append(join(dirpath,f))
                inputs.append(os.path.join(dirpath,f))
        #for p in inputs:
        #    self.arr = np.append(self.arr, self.inst.trackIn(p))
        arr = np.asarray(Parallel(-1,verbose=5)(delayed(self.inst.trackIn)(p) for p in inputs))
        arr = np.resize(arr,len(arr),)
        self.saveWork(arr,'rawmidi',20)
        
        index = np.argwhere(arr==[None])
        arr = np.delete(arr,index)
        temparr = arr
        print("original values:\n\n\n\n\n")
        print(np.resize(temparr,(len(temparr)//8,8)))
        result = kNN.doKMeans().begin(arr)


FileIO().loadWork('kmeans',"C:\\Users\\root\\Desktop")