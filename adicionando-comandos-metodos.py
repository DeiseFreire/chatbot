# --------------------------------------------------------------------------------------------
# Fonte da ideia:
# 7 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - ADICIONANDO COMANDOS MÉTODOS
# https://www.youtube.com/watch?v=lbvshOmPzYA&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=7
# --------------------------------------------------------------------------------------------

import speech_reconition as sr
import pyttsx3
speaker=pyttsx3.init()
bot=ChatBot('Jarvis',read_only=True)
dict_cmds={}
def load_cmds():
lines=open('cmds.txt','r').readlines()
for line in lines:
line=line.replace('\n','')
parts=line.split('\t')
dict_cmds.update({parts[0]:parts[1]}) 
def setVoice():
voices=speaker.getProperty('voices')
for voice in voices:
if voice.name=='brazil':
speaker.setProperty('voice',voice.id)
def speak(text):
speaker.say(text)
speaker.runAndWait()
def evaluate(text): # passar o comando valor
result=None
try:
result=dict_cmds[text] # assina o result = tipo de comando
except:
result=None
return result
setVoice() # setar a voz
load_cmds() # carregar comandos
