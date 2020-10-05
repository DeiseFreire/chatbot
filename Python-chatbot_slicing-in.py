# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Aula 4 - Python chatbot - slicing in
# https://www.youtube.com/watch?v=OVH-mCsP080&list=PLsMpSZTgkF5Bdh7-o3VnbpRpahOeDJONh&index=4
# -------------------------------------------------------------------------------------------

'''
[w1lls@Matrix ~] $ vim chatbot.py
[w1lls@Matrix ~] $ python chatbot.py
Olá, qual o seu nome?
>: O meu nome é Will
Muito prazer O meu nome é Will
[w1lls@Matrix ~] $ 
'''
'''
>>> r[0]
'O'
>>> r[1] 
' '
>>> r[2]
'm'
>>> r[-1]
'l'
>>> r[-2]
'l'
>>> r[-3]
'i'
>>> r[0:4]
'O me'
>>> r[0:5]
'O meu'
>>> r[5]
' '
>>> r[14:]
'Will'
>>> r[:14]
'O meu nome é  '
>>> '''

print('Olá, qual o seu nome?')
nome=input('>: ')
if 'O meu nome é ' in nome:
nome = nome[14:]
if nome == 'Raimundo':
print ('Eaew '+nome)
else:
print('Muito prazer '+nome)

'''
w1lls@Matrix ~] $ vim chatbot.py
[w1lls@Matrix ~] $ python chatbot.py
Olá, qual o seu nome?
>: O meu nome é Will
Muito prazer O meu nome é Will
w1lls@Matrix ~] $ vim chatbot.py
[w1lls@Matrix ~] $ python chatbot.py 
Olá, qual o seu nome?
>: O meu nome é Will
Muito prazer Will
[w1lls@Matrix ~] $ python chatbot.py
Olá, qual o seu nome?
Will
Muito prazer Will
[w1lls@Matrix ~] $ python chatbot.py
Olá, qual o seu nome?
>: O meu nome é Jonasvildo
Muito prazer Jonasvildo
[w1lls@Matrix ~] $'''
