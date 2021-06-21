import sys
import mido
import rtmidi

controls = {
    'soft/practice': {'control': 67, 'value': range(0,127)},
    'sostenuto': {'control': 66, 'value': range(0,127)},
    'sustain': { 'control': 64, 'value': range(0,127)}
}

def init():
    # mido supports several backends - rtmidi is default
    mido.Backend('mido.backends.rtmidi')

    port_names = mido.get_input_names()

    port_connected = False
    if (len(port_names) > 0):
        port_connected = True

    if (port_connected is False):
        print('No port names found. Is midi device plugged in?')
        sys.exit()
    else:
        print('List of midi input ports: ', port_names)
        print('List of midi output ports: ', mido.get_output_names())

        # assume first midi port is the correct one for now
        midi_port = port_names[0]
        print('Midi port selected: ', midi_port)

        opened_input_port = mido.open_input(midi_port)
        print('Midi port opened: ', opened_input_port)

        capture_messages(opened_input_port)


def capture_messages(opened_port):
    with opened_port as inport:
        for message in inport:
            print(message)


init()