# -------------------------------------------------------------------------------------------
# Fonte da ideia:
# #2 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - SÍNTESE DE VOZ
# https://www.youtube.com/watch?v=AVPPCBBXPh8&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=2
# -------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# importando os módulos do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
“””
import os
import speech_recognition as sr
import pyttsx3
speaker=pyttsx3.init()
bot = ChatBot('Jarvis', read_only=True)
bot.set_trainer(ListTrainer)  # definir treinamento
for _file in os.listdir('chats'):  # percorrer todos os arquivos em chats
    lines = open('chats/' + _file, 'r').readlines()  # vamos ler linhas
bot.train(lines)"""
def speak(text):
speaker.say(text)
speaker.runAndWait()
"""
from pocketsphinx import LiveSpeech 
speech = LiveSpeech(
verbose=False,
sampling_rate=16000,
buffer_size=2018,
no_search=False,
full_utt=True,
hmm='model',
lm='model.lm.bin',
dic='model.dic')
for phrase in speech:
response=bot.get_response(phrase)
print('Você disse: ',phrase) 
print('Bot: ', response)
speak(response)
r = sr.Recognizer()
with
sr.Microphone() as s:
r.adjust_for_ambient_noise(s)
while True:
try
    audio = r.listen(s)
    speech = r.recognize(audio, language='pt')
    print('Você disse: ', speech) 
response=bot.get_response(speech)
print('Bot: ', response)
speak(response)
except:
speak('Algum erro ocorreu.')
“””
