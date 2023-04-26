from microbit import *
import math

# Function to send MIDI note on message
def midiNoteOn(chan, n, vel):
    MIDI_NOTE_ON = 0x90
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel])
    uart.write(msg)

# Function to send MIDI note off message
def midiNoteOff(chan, n, vel):
    MIDI_NOTE_OFF = 0x80
    if chan > 15:
        return
    if n > 127:
        return
    if vel > 127:
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel])
    uart.write(msg)

# Function to send MIDI control change message
def midiControlChange(chan, n, value):
    MIDI_CC = 0xB0
    if chan > 15:
        return
    if n > 127:
        return
    if value > 127:
        return
    msg = bytes([MIDI_CC | chan, n, value])
    uart.write(msg)

# Function to initialize the UART communication
def Start():
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)

# Start UART communication
Start()

# Initialize variables
lastA = False
lastB = False
lastC = False
lastD = False
BUTTON_A_NOTE = 31
BUTTON_B_NOTE = 32
SHAKE_NOTE = 33
BUTTON_Ex_Note = 34
last_tilt = 0
last_pot = 0

# Main loop
while True:
    # Read the value of potentiometer and send control change message
    pot = pin2.read_analog()
    if last_pot != pot:
        velocity = math.floor(pot / 1024 * 127)
        midiControlChange(0, 30, velocity)
    last_pot = pot

    # Check button presses and accelerometer gestures
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    c = accelerometer.current_gesture()
    d = pin1.is_touched()

    # Send MIDI messages for button A
    if a is True and lastA is False:
        midiNoteOn(0, BUTTON_A_NOTE, 127)
    elif a is False and lastA is True:
        midiNoteOff(0, 0, 127)

    # Send MIDI messages for button B
    if b is True and lastB is False:
        midiNoteOn(0, BUTTON_B_NOTE, 127)
    elif b is False and lastB is True:
        midiNoteOff(0, 0, 127)

    # Send MIDI messages for shaking gesture
    if (c == "shake") and (lastC != "shake"):
        midiNoteOn(0, SHAKE_NOTE, 127)
    elif (c != "shake") and (lastC == "shake"):
        midiNoteOff(0, 0, 127)

    # Send MIDI messages for touch pin1
    if d is True and lastD is False:
        midiNoteOn(0, BUTTON_Ex_Note, 127)
    elif d is False and lastD is True:
        midiNoteOff(0, 0, 127)

    # Update last states
    lastA = a
    lastB = b
    lastC = c
    lastD = d

    # Send MIDI control change messages based on tilt in Y axis
    current_tilt = accelerometer.get_y()
    if current_tilt != last_tilt:
        mod_y = math.floor(math.fabs((((current_tilt + 1024) / 2048) * 127)))
        midiControlChange(0, 10, mod_y)
        last_tilt = current_tilt

    # Wait for 10 milliseconds
    sleep(10)

    # Send MIDI control change messages based on tilt in X axis
    current_tilt = accelerometer.get_x()
    if current_tilt != last_tilt:
        mod_y = math.floor(math.fabs((((current_tilt + 1024) / 2048) * 127)))
        midiControlChange(0, 20, mod_y)
        last_tilt = current_tilt

    # Wait for 10 milliseconds
    sleep(10)

