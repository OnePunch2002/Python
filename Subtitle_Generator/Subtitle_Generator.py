# First we have to install SpeechRecognizer package by using the command "pip install SpeechRecognition" in the terminal.
import speech_recognition as sr



# Recognizer class basically has instances which are used to recognise speech. Each instance has seven methods to recognize speech from any audio source using various APIs
r = sr.Recognizer()


# To work with microphones we have installed PyAudio package in Python by running the command "pip install PyAudio" in the terminal.

# Microphone class is used to take audio source from the microphone instead of any other audio source.
with sr.Microphone() as source:
    print("Speak Anything :")


    # To capture the input from microphone we use the listen methord.
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Say some word 😒")


