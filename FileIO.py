from pandas.io import pickle
from pandas import read_pickle
from os import walk, path
from os.path import exists, abspath, expanduser, join
import os
from joblib import Parallel, delayed
import multiprocessing
import PrepareForLearning
import numpy as np
import kNN

class FileIO:
    _PATH = os.path.expanduser("~\\Desktop")
    """description of class"""
    def __init__(self, **kwargs):
        self.inst = None

    def saveWork(self, obj, quick_descr, overwrite, ntries, _path=_PATH):
        if _path != FileIO._PATH:
            FileIO._PATH = _path
        for i in range(0,ntries):
            _path = abspath(FileIO._PATH.format(quick_descr,i))
            if overwrite or not exists(_path):
                pickle.to_pickle(obj,_path)
                return None

    def loadWork(self, filenamepart ,_path):
        if _path != FileIO._PATH:
           FileIO._PATH = _path
        fns = os.listdir(os.path.dirname(_path))
        refobj = []
        for f in fns:
            if filenamepart in str(f):
                refobj.append(read_pickle(os.path.join(os.path.dirname(_path),f)))
        return refobj
  

    def getfilefromuser(self):
        self.inst = PrepareForLearning.PrepareForLearning()
        inputs = []
        if len(self.loadWork('rawmidi',FileIO._PATH)) > 0:
           arr = self.loadWork('rawmidi',FileIO._PATH)
        else:
            curdir = abspath(expanduser("~\\Source\\Repos\\midi_quantizer\\midiFiles"))
            curdir = "C:\\Documents and Settings\\philiph\\Documents\\Rep\\midi_quantizer\\small__midi" #for different file structure
            for (dirpath, dirnames, filenames) in walk(curdir):
                for f in [x for x in filenames if str(x).endswith("mid")]:
                    #inputs.append(join(dirpath,f))
                    inputs.append(join(dirpath,f))
            #for p in inputs:
            #    self.arr = np.append(self.arr, self.inst.trackIn(p))
            arr = np.asarray(Parallel(-1,verbose=5)(delayed(self.inst.trackIn)(p) for p in inputs))
        arr = np.resize(arr,len(arr),)
        self.saveWork(arr,'rawmidi',False,20)
        
        index = np.argwhere(arr==[None])
        arr = np.delete(arr,index)
        temparr = arr
        print("original values:\n\n\n\n\n")
        print(np.resize(temparr,(len(temparr)//8,8)))
        kNN.doKMeans().begin(arr)


