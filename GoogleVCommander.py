__author__ = 'deddo_000'

import speech_recognition as speech

r = speech.Recognizer()
command = str()

debugMode = 2


with speech.Microphone() as source:
    print("Starting Listening")
    TemporaryAudioFile = r.listen(source)
    print("Sample Gathered")

def DebugModeTest():
    try:
        print("You said " + r.recognize(TemporaryAudioFile))    # recognize speech using Google Speech Recognition
        command = r.recognize(TemporaryAudioFile) # stores the text output from last voice input
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")

def SwitchMicOn():
    pass

def SwitchMicOff():
    pass

def voiceCaptureOn():
    pass

def voiceCaptureOff():
    pass



# Step One - Debug Test
if debugMode:
    DebugModeTest()
elif debugMode is not 1 and not 0:
    print("Its Boolean You Retard!")
