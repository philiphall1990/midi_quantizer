from builtins import round

import mido
from mido import *
from threading import *
import time
import sys

class readMidiIn():

    def __init__(self):
        listOfPorts = mido.get_input_names()
        for i in range(0, len(listOfPorts)-1):
            print('{0}) {1}\n'.format(i + 1, listOfPorts[i]))
        portNo = input("Select the  desired port by typing the number of its listing.")
        if int(portNo) < 0:
            exit()
        messagesAsTimes  = []
        mido.open_input(str(listOfPorts[int(portNo)-1]), virtual=False, callback=self.actOnInput(messagesAsTimes))
        #TEST1
        self.normalize_times([0.832,0.982,1.24,8.53,9.43])

     # self.normalize_times(messagesAsTimes)

    def actOnInput(self, messagesAsTimes):
        if len(messagesAsTimes) is 0:
            messagesAsTimes.append(time.time())
        p = mido.Parser()
        while p.pending() > 0:
            messagesAsTimes.append(p.get_message())
        return 0


