import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
  r.adjust_for_ambient_noise(source,duration=5)
  r.dynamic_energy_threshold = True
  print("Say something!")
  audio = r.listen(source)
try:
  print("You said:" + r.recognize_google(audio))
except sr.UnknownValueError:
  print("Google speech Recognition could not understand the audio")
except sr.RequestError as e:
  print("could not request results from google speech recognition service; {0}".format(e))

