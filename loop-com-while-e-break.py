# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Aula 5 - Python chatbot - Loops com while e break
# https://www.youtube.com/watch?v=UQORiDqVmBA&list=PLsMpSZTgkF5Bdh7-o3VnbpRpahOeDJONh&index=5
# -------------------------------------------------------------------------------------------

print ('Olá, qual o seu nome?')
nome=input('>: ') 
if 'O meu nome eh ' in nome: 
nome=nome[14:]
if nome=='Raimundo': 
print(Eaew '+nome) 
else: 
print('Muito prazer '+nome)
# while 2==2: 
# print(' ') 
while True: 
resposta = input ('>: ') 
if resposta == 'tchau': 
break 
else: 
print('Digite outra coisa') # impressão
print('Tchau tchau')

