def imputar():
    texto = input('>: ').lower()
    texto = texto.replace('eh', 'é')
    return texto


def interacaoInicial(nome):
    if 'meu nome é ' in nome:  # in significa 'estar presente'
        nome = nome[10:]

    nome = nome.title()
    if nome in conhecidos:
        comprimento = 'e ai caralho, fmz'

    return (comprimento, nome)


conhecidos = ['Helen', 'Amanda', 'Tiago']
comprimentoPadrao = 'Muito prazer'
