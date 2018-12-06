from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
#from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    #for line in audio.splitlines():
     #   os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #text_to_speech = gTTS(text=audio, lang='en')
    #text_to_speech.save('audio.mp3')
    l="./李云龙/"+audio+".mp3"
    print(l)

    os.system('start '+l)


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        #command = r.recognize_google(audio).lower()
        command = r.recognize_google(audio,language="zh").lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    if "你好" in command:
        talkToMe(".043")
    if "厉害" in command:
        talkToMe(".008")
    elif '打开' in command:
        reg_ex = re.search('打开(.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass


#loop to continue executing multiple commands
while True:
    assistant(myCommand())
