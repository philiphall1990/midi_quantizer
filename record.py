from itertools import count
import mido
import threading
import asyncore
import itertools


class Record():
    def __init__(self):
        self.toFile = []
        self.file = []

    def callbackFunction(self, indev):
        for msg in indev:
            self.toFile.append(msg)

    def getDevice(self):
        for i, devs in mido.get_input_names():
            print(str(i) + str(devs[i]))
        port = devs[input("select")]
        indev = mido.ports.BaseInput
        indev(port, virtual=False, callback=threading.Thread(self.callbackFunction(indev)).run())
