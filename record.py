from itertools import count
import threading
import mido
import asyncore
import itertools

class Devices:
    def __init__(self):
        self.toFile = []
        self.file = []

    def callbackFunction(self, indev):
        for msg in indev:
            self.toFile.append(msg)


    def getDevice(self = None):
        devs = mido.get_input_names()
        for i in range(0,len(devs)):
            print(str(i) + str(devs[i]))
        port = devs[int(input("Select  device by its number only"))]
        indev = mido.ports.BaseInput(port)
        indev(port, virtual=False, callback=threading.Thread(self.callbackFunction(indev)).run())
