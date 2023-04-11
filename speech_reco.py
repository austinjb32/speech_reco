import speech_recognition as sr
import whisper
import pyperclip as pyc
import keyboard as ky

r = sr.Recognizer()
model=whisper.load_model('base')


with sr.Microphone() as source:
    
    r.adjust_for_ambient_noise(source)
    print("Listening...")

    audio = r.listen(source, phrase_time_limit=5)

try:
  
    text = r.recognize_google(audio)
    # result= model.transcribe(audio,fp16=False)
    

    print(f"You said: {text}")
    # print(f"Whisper:{result['text']}")
    ky.write(text)
except sr.UnknownValueError:
  
    print("Could not understand audio")
except sr.RequestError as e:

    print(f"Could not request results from Google Speech Recognition service; {e}")
