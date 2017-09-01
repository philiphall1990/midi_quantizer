import FileIO
from builtins import round
import mido
from threading import *
import time
import record

class readMidiIn:
    def __init__(self):
        self.LIVE_OR_FILE = 2#input("Do you want to work on:1) Live midi in from a device;/n2)A midi file from filesystem")

    def read(self):
         if str(self.LIVE_OR_FILE) == "1":
            return record.Devices.getDevice()
         else:
            fio = FileIO.FileIO()
            return fio.getfilefromuser()
        