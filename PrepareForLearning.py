from os import path
from pandas.io import pickle
import kNN
import mido
from mido import Message, MidiTrack
import numpy as np
from matplotlib import pyplot as plt

class PrepareForLearning:

    def __init__(self):
        self.notetimes_i0 = np.empty((0,8))
        self.notetimes_i1 = np.empty((0,0),dtype=np.ndarray)

    def trackIn(self, path):
        self.notetimes_i1 = np.empty((1,-1),dtype=np.ndarray)
        liveNoteDict = {}
        try:
            mid_file = mido.MidiFile(path)
            abs_time = 0
            for trck in mid_file.tracks:
                for msg in trck:
                    abs_time += msg.time
                    if msg.type == 'note_on':
                        liveNoteDict.update({msg.note : abs_time})
                    if msg.type == 'note_off':
                         temp = (abs_time - liveNoteDict.pop(msg.note,0))
                         if type(temp) == type(5.0):
                            if not (temp > (np.copy(self.notetimes_i0).mean()*100)):
                                self.notetimes_i0 = np.append(self.notetimes_i0,temp,0)
                                if len(self.notetimes_i0) % 8 == 0:
                                    self.notetimes_i1 = np.append(self.notetimes_i1,self.notetimes_i0,0)
                                    self.notetimes_i0 = np.empty(1,8)

                
                    
        except Exception as e:
            print(str.format("{0}-{1}",path,str(e)))

        return self.notetimes_i0