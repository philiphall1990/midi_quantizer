import sys
import record
import read_midi_in
import sys
def main(args=None):
    """The main routine."""
    rm = read_midi_in.readMidiIn()
    r = record.Record()
    r.getDevice()

if __name__ == "__main__":
    main()