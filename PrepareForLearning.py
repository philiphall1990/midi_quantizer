import kNN
import mido
from mido import Message, MidiTrack

class PrepareForLearning:

    def trackIn(self, path):
        liveNoteDict = {}
        notetimes = []

       
        trck = mido.MidiFile(path)
        abs_time = 0
        for msg in trck:
            abs_time += msg.time
            msg_last = msg
            if msg.type == 'note_on':
                liveNoteDict.update({msg.note : abs_time})
            if msg.type == 'note_off':
                 notetimes.append((abs_time - liveNoteDict.pop(msg.note,0)))

            kNN.ski()