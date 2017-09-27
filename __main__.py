import sys
import record
import sys
import read_midi_in

def main(args=None):
    """The main routine."""
    rm = read_midi_in.readMidiIn()
    rm.read()
   # r = record.Devices()
   # r.getDevice()

if __name__ == "__main__":
    main()