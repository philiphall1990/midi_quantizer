from os import path
from pandas.io import pickle
import kNN
import mido
from mido import Message, MidiTrack
import numpy as np
from matplotlib import pyplot as plt

class PrepareForLearning:

    def __init__(self):
        self.plot = plt.show(block=False)
        self.notetimes = []

    def trackIn(self, path):
        self.notetimes = []
        liveNoteDict = {}
        try:
            trck = mido.MidiFile(path)
            abs_time = 0
            for msg in trck:
                abs_time += msg.time
                if msg.type == 'note_on':
                    liveNoteDict.update({msg.note : abs_time})
                if msg.type == 'note_off':
                     temp = (abs_time - liveNoteDict.pop(msg.note,0))
                     if type(temp) == type(5.0):
                        if not (temp > (np.copy(self.notetimes).mean()*100)):
                            self.notetimes.append(temp) 
                    
        except Exception as e:
            print(str.format("{0}-{1}",path,str(e)))

        return self.notetimes