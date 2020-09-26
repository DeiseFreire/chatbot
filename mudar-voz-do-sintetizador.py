  
# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# 4 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - MUDAR VOZ DO SINTETIZADOR
# https://www.youtube.com/watch?v=yJqmTLvAI3s&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=4
# -------------------------------------------------------------------------------------------

import pyttsx3
engine = pyttsx3.init()
voices=engine.getProperty('voices')
for voice in voices:
if voice.name == 'brazil':
engine.setProperty('voice',voice.id)
engine.say('oi bom dia como vai')
engine.runAndWait()
