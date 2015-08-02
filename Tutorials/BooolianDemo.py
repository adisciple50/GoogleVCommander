__author__ = 'deddo_000'

 # import speech_recognition as speech

# r = speech.Recognizer()
command = str()

debugMode = False

"""
with speech.Microphone() as source:
    print("Starting Listening")
    TemporaryAudioFile = r.listen()
    print("Sample Gathered")
"""
"""
def DebugModeTest():
    try:
        print("You said " + r.recognize(TemporaryAudioFile))    # recognize speech using Google Speech Recognition
        command = r.recognize(TemporaryAudioFile) # stores the text output from last voice input
    except LookupError:                            # speech is unintelligible
        print("Could not understand audio")
"""

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
    print("Correct - Boolian is set")
    # DebugModeTest()
else:
    print("Debug Mode Is Off")

if type(debugMode) is not bool:
    print("Its Boolean You Retard!")
