# GGD_Voice_Changer
This is a voice changer designed for use by anchors or gamers. It can be used to give interesting effects to the sound received by the microphone through gesture control. You can also play the sound effects and music you want quickly with the buttons and adjust the gain with the knob.

## Features

You can adjust the pitch and distortion of the voice with gesture control, trigger interesting sound effects with the buttons, or talk underwater.
## File description

* [GGD_voice_changer.py](GGD_voice_changer.py) is the code that gives the micro: bit function. It includes the use of gestures, knob and keys, the definition of MIDI note and MIDI Control Change functions.

* [GGD_Voice_Changer_Interface.maxpat](GGD_Voice_Changer_Interface.maxpat) is a patch file for Max, a sort of Interface for the GGD voice changer, which is designed to interact with the micro:bit function to allow the use of the voice changer.

* [gizmo_loadme.maxpat](gizmo_loadme.maxpat) is a sub-patch of the previous GGD_Voice_Changer_Interface.maxpat, which is used to implement the effect of changing the pitch.

## .wav files

These audio files are triggered to play via keystrokes. The three audio files are Pigeon, Assassin and Blister. The Pigeon and Assassin refer to the skill sound effects of the characters in the game GooseGooseDuck. The user has the flexibility to use other sound effects/music that they x want to use by changing the audio path in the Interface file.
