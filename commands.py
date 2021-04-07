from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
from os import system


GR = {

    ("привет", "привет друг!", "хаю-хай", "салют", "здарова", "салам алейкум!") : ("Привет друг!", "хаю-хай", "Салют", "здарова", "Салам алейкум!", "Привет"),
    ("как дела", "как делишки", "как ты", "как ты братан") : ("спасибо, неплохо, у вас ?", "так себе...", "пойдёт"),
    ("как вас зовут", "ваше имя", "фио") : ("Мокаева Лейля Борисовна", "можете называть меня Лейля", "Лейлюш)"),
    ("лейля", "лейлюш", "мокаева лейля борисовна", "леля") : ("Ауу", "что?", "к вашим услугам")
}

ON = {

    "открыть калькулятор" : r"%windir%\system32\calc.exe",
    "открыть броузер" : r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "открыть рисовалку" : r"%windir%\system32\mspaint.exe",
    "открыть проводник" : r"%windir%\explorer.exe"

}

def listen_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        our_speech = r.recognize_google(audio, language="en")
        return our_speech
    except Exception as ex:
        print(ex)




def do_this_command(message):
    if type(message) == str:
        message = message.lower()
        for k in ON:
            if message in k:
                system(ON[k])

        for k, v in GR.items():
            for elem in k:
                if message in elem:
                    return say_message(random.choice(v))

        if message == "спой песенку":
            return say_message("я от бабушки ушёл я от дедушки ушёл, и от тебя уйду")



def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)







