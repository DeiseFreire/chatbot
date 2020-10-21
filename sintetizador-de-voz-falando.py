# -------------------------------------------------------------------------------------------
# Fonte da ideia:
# 8 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - SINTETIZADOR DE VOZ FALANDO
# https://www.youtube.com/watch?v=z0qEv6Rt1p8&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=8
# -------------------------------------------------------------------------------------------

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
def run_cmd(cmd_type):
result=None
if cmd_type=='asktime':
now=datetime.now()
result='São '+str(now.hour)+ ' horas e ' +str(now.minute)+ ' minutos.'
elif cmd_type=='askdate':
now=datetime.now()
months=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
result='Hoje é ' +str(now.day)+ ' de '+months[now.month-1]
else:
result=None
return result
setVoice() # setar a voz
load_cmds() # carregar comandos 
for k, v in dict_cmds.items():
print(k, '=====>', v)
from pocketsphinx import pocketsphinx, Jsgf,FsgModel
# create decoder object
config=pocketsphinx.Decoder.default_config()
config.set_string("hmm",'model') # set the path of hidden Markov model (HMM) parameter files
config.set_string("-lm",'model.lm.bin')
config.set_string("-dict",'model.dict')
config.set_string("-lognf",os.devnull) # disable logging (logging causes unwanted output in terminal)
decoder=pocketsphinx.Decoder(config)
def recognize_pt(audio):
raw_data=audio.get_raw_data(convert_rate=16000,convert_width=2)
decoder.start_utt() #begin utterance processing
decoder.process_raw(raw_data,False,True) # process audio data with recognition enabled (no_search=False), as a full utterance(full_utt=True)
decoder.end_utt() # stop utterance processing
hypothesis=decoder.hyp()
if hypothesis is not None:
return hypothesis.hypstr
return None
r=sr.Recognizer()
import traceback
with sr.Microphone() as s:
r.adjust_for_ambient_noise(s)
while True:
audio=r.listen(s)
speech=recognize_pt(audio) #usando o pocketsphinx
response=run_cmd(evaluate(speech))
if response==None:
print('Voce disse: ',speech)
print('Bot: ',response)
speak(response)
r=sr.Recognizer()
import traceback
