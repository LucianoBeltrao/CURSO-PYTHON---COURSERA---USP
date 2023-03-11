import re

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

sentenca = texto[:]

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

frase = sentenca[:]

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

lista_palavras = frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

lista_palavras = frase[:]

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

palavras = frase.split()

def conta_tamanho_das_palavras(palavras):
    t=0
    for c in palavras:
        t=t+len(c)
    tamanho_medio = t//len(palavras)
    float(tamanho_medio)
    print (float(tamanho_medio))

def conta_total_de_letras(palavras):
    t=0
    for c in palavras:
        t=t+len(c)
    return t


def tipetoken():
    tipetoken = n_palavras_diferentes(lista_palavras)/ len(palavras)
    print(tipetoken)

def hapax():
    hapax = n_palavras_unicas(lista_palavras)/len(palavras)
    print(hapax)

    """soma do número de caracteres em todas as sentencas / número de sentencas"""
def tamanho_medio_sentenca(): 
    d=len(texto)/len(separa_sentencas(texto))
    print(d)

# até aqui tudo ok#
    """soma do número de caracteres em todas as sentencas / número de sentencas"""
def complexidade_sentenca():
    e=len(separa_sentencas(texto))/len(separa_frases(sentenca))
    print(e)
    """Numero total de frases / numero de sentecas"""
def tamanho_medio_da_frase():
    separa_frases(sentenca)
    """Soma do numero das caracteres en casa frase / número de frases no texto"""

def caracteres_sentenca():
   b=len(separa_sentencas(texto))
   print(b)


def caracteres_frase(frase):
    g=0
    for b in frase:
        g=g+len(b)
    print(g)

    
   
    



