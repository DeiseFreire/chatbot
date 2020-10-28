# -------------------------------------------------------------------------------------------
# Fonte da ideia:
# Aula 6 - Python chatbot - Loops com for e listas
# https://www.youtube.com/watch?v=PCo5X2jfIzg&list=PLsMpSZTgkF5Bdh7-o3VnbpRpahOeDJONh&index=7
# -------------------------------------------------------------------------------------------

print('Olá, qual o seu nome?')
nome=input('>: ')
if 'O meu nome eh ' in nome:
nome=nome[14:]
if nome=='Raimundo':
print(Eaew '+nome)
else:
print('Muito prazer '+nome)
if nome=='Will':
print('Eaew '+nome)
else:
print('Muito prazer '+nome)
while True:
resposta=input('>: ')
if resposta=='tchau':
break
else:
print('Digite outra coisa')
print('Tchau tchau!')
