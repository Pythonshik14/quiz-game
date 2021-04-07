import pandas as pd
from VoiceHelper.commands import *

from random import randint, choice
def do_cmd(mess, ques):
    if type(mess) == str:
        mess = mess.lower()
        if " "+mess ==  ques[1]:
            return say_message(choice(["Верно!", "молодец, угадал!", "Правильно", "совершенно верно!"]))
        else:
            return say_message(choice(["Не правильно", "нет дорогой", "не верно"]))

def random_question():
    with open("quesRepl.csv", 'r', encoding='utf8') as fily:
        text = fily.read()
        new_text = text.replace(",", "")
        new_text = text.replace(";", ",")


    with open("quesRepl.csv", 'w', encoding='utf8') as wr:
        wr.write(new_text)

    data = pd.read_csv("quesRepl.csv", header=None)
    data.columns = ["Question", "Reply"]
    questions = data['Question']
    replys = data['Reply']
    ques = randint(0, len(data['Reply'])-1)

    return questions[ques], replys[ques]

while 1:
   text = random_question()
  
   say_message(text[0])

   inp = listen_command()


   if inp == "stop" or inp == 'break':
       run = False

   else:
       do_cmd(inp,  text)
