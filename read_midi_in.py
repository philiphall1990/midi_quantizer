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
        fio.getfilefromuser()
        return input("Press any key to exit.")
        