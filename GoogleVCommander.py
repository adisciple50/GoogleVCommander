__author__ = 'deddo_000'

import speech_recognition as speech

r = speech.Recognizer()
command = str()


with speech.Microphone() as source:
    print("Starting Listening")
    TemporaryAudioFile = r.listen()
    print("Sample Gathered")

try:
    print("You said " + r.recognize(TemporaryAudioFile))    # recognize speech using Google Speech Recognition
    command = r.recognize(TemporaryAudioFile)
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")

