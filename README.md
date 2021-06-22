# midi_capture
Project for capturing MIDI from digital instruments

## Purpose
The purpose of this project is to capture MIDI input data from a digital piano. The initial idea was to capture MIDI data and then to convert MIDI messages from the digital piano into an outport stream (via another port) and to convert MIDI messages into CSV and JSON formats. The data collectedis for future data analytics projects and well as future audio-processing projects.

## Relies on
* mido
* rtmidi

## Goals
* Convert MIDI data to CSV
* Send MIDI data to an output port for use
