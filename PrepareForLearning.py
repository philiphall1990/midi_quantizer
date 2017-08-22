import mido
from mido import Message, MidiTrack

class PrepareForLearning:

    def trackIn(self, track):
        trackTimes = []
        trackNotes = []
        path = "C:\\Users\\root\\Dropbox\\4731.mid"
        trck = mido.MidiFile(path)
        for msg in trck:
            if msg.type == 'note_on':
                trackTimes.append(msg.time)
            if msg.type == 'note_off':
                trackTimes[len(trackTimes) -1] = msg.time - trackTimes[len(trackTimes)-1]
                trackNotes.append(msg.note)
