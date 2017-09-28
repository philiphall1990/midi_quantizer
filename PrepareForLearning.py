from os import path
from pandas.io import pickle
import kNN
import mido
from mido import Message, MidiTrack
import numpy as np
from matplotlib import pyplot as plt

class PrepareForLearning:

    def __init__(self):
        self.notetimes = np.empty((0,0))
        

    def trackIn(self, path):
        self.notetimes = np.empty((0,0))
        liveNoteDict = {}
        try:
            mid_file = mido.MidiFile(path)
            abs_time = 0
            for trck in mid_file.tracks:
                for msg in trck:                   
                    if msg.type == 'note_on' and not msg.velocity == 0:
                        abs_time += msg.time
                        liveNoteDict.update({msg.note : abs_time})
                    if msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                        abs_time += msg.time
                        temp = float(abs_time - liveNoteDict.pop(msg.note,0))
                        if not (temp > (self.notetimes.mean()*100)):
                            self.notetimes = np.append(self.notetimes,[temp])              
                    
        except Exception as e:
            print(str.format("{0}-{1}",path,str(e)))
        return self.notetimes