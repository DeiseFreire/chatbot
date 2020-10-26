# ------------------------------------------------------------------------------------------
# Fonte da ideia: 
# 9 COMO CRIAR O SEU ASSISTENTE VIRTUAL EM PYTHON - BUSCAR DEFINIÇÃO NA WIKIPÉDIA
# https://www.youtube.com/watch?v=mdSdD3gre7E&list=PL39zyvnHdXh9M1Nk9XXmhKOzP0o9_9Eba&index=9
# ------------------------------------------------------------------------------------------

def recognize_pt(audio):
raw_data = audio.get_raw_data(convert_rate=16000,convert_width=2)
decoder.start_utt() # begin utterance processing 
decoder.process_raw(raw_data,False,True) # process audio data with recognition enabled (no_search = False), as a full utterance (full_utt = true)
decoder.end_utt() # stop utterance processing
hypothesis = decoder.hyp()
if hypothesis is not None:
return hypothesis.hypstr
return None
r = sr.Recognizer()
import tracback
with sr.Microphone() as s:
r.adjust_for_ambient_noise(s)
while True:
audi = r.listen(s)
#speech = recognize_pt(audio) # usando o pocketsphinx
speech = r.recognize_google(audio,language'pt').lower()
response = run_cmd(evaluate(speech))
if response == None:
response = bot.get_response(speech)
print('você disse: ',speech)
print('Bot: ',response)
speak(response)
