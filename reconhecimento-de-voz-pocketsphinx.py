# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# 3 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - RECONHECIMENTO DE VOZ POCKETSPHINX
# https://www.youtube.com/watch?v=wCr6DiwmZv8&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=3
# -------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
# importando os módulos do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
"""
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
buffer_size=2048,
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
"""
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
# create decoder objetct
config = pocketsphinx.Decoder.default_config()
config.set_string("-hmm", 'model')  # set the path of the hidden Markov model (HMM) parameter files
config.set_string("-lm", 'model.lm.bin')
config.set_string("-dict", 'model.dic')
config.set_string("-logfn",os.devnull) # disable logging (logging causes unwanted output in terminal)
decoder = pocketsphinx.Decoder(config)
def recognize_pt(audio):
raw_data = audio.get_raw_data(convert_rate=16000,convert_width=2) 
decoder.start_utt() # begin utterance processing 
decoder.process_raw(raw_data,False,True) # process audio data with recognition enabled (no_search = False),as a full utterance (full_utt=True)
decoder.end_utt() # stop utterance processing
hypothesis = decoder.hyp()
if hypothesis is not None: return hypothesis.hypstr
return None
r = sr.Recognizer()
import traceback
with sr.Microphone() as s:
r.adjust_for_ambient_noise(s)
while True:
try
audio = r.listen(s)
speech=recognize_pt(audio)
print('Você disse: ', speech) 
response=bot.get_response(speech) 
print('Bot: ', response)
speak(response)
except:
"""


