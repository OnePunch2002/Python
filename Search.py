import webbrowser as wb
import speech_recognition as sr
# Recognizer class basically has instances which are used to recognise speech. Each instance has seven methods to recognize speech from any audio source using various APIs
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
# To work with microphones we have installed PyAudio package in Python by running the command "pip install PyAudio" in the terminal.

# Microphone class is used to take audio source from the microphone instead of any other audio source.
with sr.Microphone() as source:
    print('[search youtube: search google]')
    print("Speak Anything :")
    # To capture the input from microphone we use the listen methord.
    audio = r3.listen(source)

if 'youtube' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com'

    try:
        # this is API used to 
        text = r1.recognize_google(audio)
        print(wb.get)
        wb.get().open_new(url+wb.get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'google' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.google.co.in'

    try:
        # this is API used to 
        text = r1.recognize_google(audio)
        print(wb.get)
        wb.get().open_new(url+wb.get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))
        
 