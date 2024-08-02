# speech regn is an api provided by google.. u enter ur audio file it gives u text
#record file and convert to dot wav extension
# download as py -m pip install modulename in cmd

import speech_recognition as sr
audfile=("WEEK5\Recording.wav")
 #use ad file as source
 #initialse a recogniser read the file  print the results or any of the two error

r=sr.Recognizer()
with sr.AudioFile(audfile) as source:
 audio=r.record(source) #fn to read aud file

try:
 print("aud file contains \n "+r.recognize_google(audio))
except sr.UnknownValueError:
 print("googlr sr cant understand audio")
except sr.RequestError:
 print("coudnt get results from google s r")

 #exception is a type of error