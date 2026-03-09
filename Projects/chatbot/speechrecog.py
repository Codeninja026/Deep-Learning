
import speech_recognition as sr


recog = sr.Recognizer()

with sr.Microphone() as source:
    print("say something....")
    audio = recog.listen(source)

try:
    text = recog.recognize_google(audio)
    print("You said: ->  ",text)


except sr.UnknownValueError:
    print("Error")