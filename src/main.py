from interacoes import *

print('olá, vamos começar! poderia informar seu nome?')
print(interacaoInicial(imputar()))

while True:
    resposta = input('>: ')
    if resposta == 'tchau':
        print('Até mais!')
        break

    print('Em que posso ajudar?')
