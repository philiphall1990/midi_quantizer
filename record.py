from itertools import count
from mido.ports import BaseInput
import threading
import mido
import itertools

class Devices:
    def __init__(self):
        self.device = subBaseInput(None)
        self.toFile = []
        self.file = []

    def callbackFunction(self):
        while not self.device.closed:
            msg = self.device.poll()
            if not msg == None:
                self.file.append(msg)
                print(str(bytes(msg)))

    def getDevice(self = None):
        devs = mido.get_input_names()
        for i in range(0,len(devs)):
            print(str(i) + str(devs[i]))
        port = devs[int(input("Select  device by its number only"))]
        indev = subBaseInput
        indev(port, virtual=False, callback=threading.Thread(self.callbackFunction()).run())
       

class subBaseInput(BaseInput):
    def __init__(self, name = '', **kwargs):
        return super().__init__(name, **kwargs)
 