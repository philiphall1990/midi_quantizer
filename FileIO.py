from pandas.io import pickle
from os import walk, path
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
        self.inst = pl.PrepareForLearning()


    def saveWork(self, obj, quick_descr, ntries, _path="C:\\Users\\root\\Desktop\\pickle-{0}-{1}"):
        for i in range(0,ntries):
            _path = path.abspath(_path.format(quick_descr,i))
            if not path.exists(_path):
                pickle.to_pickle(obj,_path)


    def getfilefromuser(self):
        inputs = []
        for (dirpath, dirnames, filenames) in walk("C:\\Users\\root\\Downloads\\130000_Pop_Rock_Classical_Videogame_EDM_MIDI_Archive[6_19_15]\\130000_Pop_Rock_Classical_Videogame_EDM_MIDI_Archive[6_19_15]\\"):
            for f in [x for x in filenames if str(x).endswith("mid")]:
                #inputs.append(join(dirpath,f))
                inputs.append(join(dirpath,f))
        self.arr = self.arr + Parallel(-1,verbose=5)(delayed(self.inst.trackIn)(p) for p in inputs)
        nw = []
        for y in self.arr:
            for a in y:
                if type(a) == type(0.89):
                    nw.append(a)
        self.arr = nw
        if type(self.arr[0]) != type(0.4):
            self.arr = [x for x in self.arr]
        self.saveWork(self.arr,'rawmidi',20)
        result = kNN.doKMeans().begin(self.arr)
        