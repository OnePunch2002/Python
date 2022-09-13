from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk()
mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0,0)
mainwindow.configure(bg='cadetblue3')

def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text

def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='darkseagreen2')

    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Comic Sans MS", 20), bg='darkseagreen2').place(x=75)

    text = Text(texttospeechwindow, height=20, width=54, font=12)
    text.place(x=5, y=60)
    
    speakbutton = Button(texttospeechwindow, text='listen', bg='darkseagreen3', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=235, y=450)

def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='plum3')

    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 20), bg='plum3').place(x=75)

    text = Text(speechtotextwindow, font=12, height=20, width=54)
    text.place(x=5, y=60)
    
    recordbutton = Button(speechtotextwindow, text='Record', bg='orchid3', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=225, y=450)

Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Brush Script MT', 20), bg='cadetblue3', wrap=True, wraplength=450).place(x=26, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='cyan4', command=TextToSpeech)
texttospeechbutton.place(x=120, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='cyan4', command=SpeechToText)
speechtotextbutton.place(x=120, y=250)

mainwindow.update()
mainwindow.mainloop()
