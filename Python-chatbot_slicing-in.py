# -------------------------------------------------------------------------------------------
# Fonte da ideia: 
# Aula 4 - Python chatbot - slicing in
# https://www.youtube.com/watch?v=OVH-mCsP080&list=PLsMpSZTgkF5Bdh7-o3VnbpRpahOeDJONh&index=4
# -------------------------------------------------------------------------------------------

print( 'Olá, qual o seu nome?' )
nome = input( '>: ' )
if 'O meu nome é ' in nome:
    nome = nome[14:]
if nome == 'Raimundo':
    print( 'Eaew ' + nome )
else:
print( 'Muito prazer ' + nome )

