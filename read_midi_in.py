from builtins import round
import mido
from threading import *
import time
import record

class readMidiIn:
    def __init__(self):
     LIVE_OR_FILE = input("Do you want to work on:1) Live midi in from a device;\n2)A midi file from filesystem")
     if str(LIVE_OR_FILE) == "1":
         record.Devices.getDevice
     else: 
         pass
    def actOnInput(self, messagesAsTimes):
        if len(messagesAsTimes) is 0:
            messagesAsTimes.append(time.time())
        p = mido.Parser()
        while p.pending() > 0:
            messagesAsTimes.append(p.get_message())
        return 0


