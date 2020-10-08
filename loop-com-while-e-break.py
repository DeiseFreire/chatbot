# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Aula 5 - Python chatbot - Loops com while e break
# https://www.youtube.com/watch?v=UQORiDqVmBA&list=PLsMpSZTgkF5Bdh7-o3VnbpRpahOeDJONh&index=5
# -------------------------------------------------------------------------------------------

print ('Olá, qual o seu nome?') # impressão
nome=input('>: ') # entrada
if 'O meu nome eh ' in nome: # e se ou se 
nome=nome[14:]
if nome=='Raimundo': # e se ou se
print(Eaew '+nome) # impressão
else: # outro
print('Muito prazer '+nome)
>>> while 2==2: # enquanto
... print(' ') # impressão
Traceback (most recent call last): # Rastrear de volta (última chamada mais recente):
File "<stdin>", line 2, i # Arquivo "<stdin>", linha 2, i
n <module> # módulo
keyboardInterrupt # interrupção do teclado
>>> n = 1
>>> while n < 3: # enquanto
... print(n)  # impressão     
... n = n + 1 
