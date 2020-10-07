# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# #6 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - ADICIONANDO COMANDOS
# https://www.youtube.com/watch?v=UTAUhkM98Oo&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=6
# -------------------------------------------------------------------------------------------

bot=ChatBot('Jarvis',read_only=True)
dict_cmds={}
def load_cmds():
lines = open('cmds.txt', 'r').readlines()
for line in lines:
line=line.replace('\n',' ')
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
setVoice() # setar a voz
load_cmds() # carregar comandos
for k,v in dict_cmds.items():
pritn(k, ' =====> ', v)
from pocketsphinx import pocketsphinx, Jsgf, FsgModel
# create decoder object
config=pocketsphinx.Decoder.default config()
config.set_string("-hmm",'model') # set the path of the hidden Markov model (HMM) parameter files
config.set_string("-lm", 'model.lm.bin')
config.set_string("-dict",'model.dic')
config.set_string("-logfn", os.devnull) # disable logging (logging causes unwanted output in terminal)

