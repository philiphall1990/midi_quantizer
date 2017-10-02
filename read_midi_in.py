import kNN
import FileIO
from builtins import round
import mido
from threading import *
import time
import record
from sklearn.preprocessing import normalize
from pandas import read_pickle

class readMidiIn:
    def read():
        fio = FileIO.FileIO()
        results = read_pickle("C:\\normalized_midi")
        kNN.doKMeans().begin(results)
        return fio.getfilefromuser()
        