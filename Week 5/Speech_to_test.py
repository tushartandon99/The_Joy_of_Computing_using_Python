import speech_recognition as sr
Audio_file=("D:\\Laptop\\Downloads\\audioo.wav")
#use audio file as source

r=sr.Recognizer()#initialize the recognizer

with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)
    #read the audio file

try :
    print("audio file contains "+ r.recognize_google(audio))
except sr.UnknownValueError:
    print ("Google speech could not understand audio")
except sr.RequestError :
    print ("couldn't get the result from google")