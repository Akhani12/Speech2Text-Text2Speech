import pyttsx3
from datetime import datetime
import speech_recognition as sr
def speak(content):
    engine = pyttsx3.init()
    engine.say(content)
    engine.runAndWait()

# Machine Speak Simple Word...
speak(content="How Are You ?")

# Machine Speak Time...
time = datetime.now().strftime("%I:%M:%S")
speak(time)

# This Is For Whenever You Want To Save File....
# engine.save_to_file('Hello World' , 'test.mp3')

# This is For Year,Month And Day...
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

speak(year)
speak(month)
speak(day)


# This Is For Hour...
hour = datetime.now().hour
speak(hour)

# For Microphone....
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Listening.....")
  audio = r.listen(source)
  speak(audio)
