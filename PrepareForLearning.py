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
        plt.ion()
        
    def trackIn(self, path):
        self.notetimes = np.empty((0,0))
        liveNoteDict = {}
        print("working on file:")
        try:
            mid_file = mido.MidiFile(path)
            print(str(mid_file))
            abs_time = 0
            for trck in mid_file.tracks:
                for msg in trck:                   
                    if msg.type == 'note_on' and not msg.velocity == 0:
                        abs_time += msg.time
                        liveNoteDict.update({msg.note : abs_time})
                    if msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                        abs_time += msg.time
                        temp = float(abs_time - liveNoteDict.pop(msg.note,0))
                        self.notetimes = np.append(self.notetimes,[temp])

                print("success!")
        except Exception as e:
            print(str.format("Failed! {0}",str(e)))
        if len(self.notetimes) == 0:
            return None
        while len(self.notetimes) % 8 != 0:
            self.notetimes = np.delete(self.notetimes,len(self.notetimes)-1)
        return self.notetimes