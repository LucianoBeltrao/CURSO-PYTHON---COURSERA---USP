def computador_escolhe_jogada(n,m):
    c=0
    while n%(m+1) !=0:
        c=c+1
        n=n-1
    if c==0:
        c=1
        n=n-c
    if c == 1:
        print()
        print('O Computador tirou uma peça')
    else:
        print()
        print('O Computador tirou', c,'peças.')
    if n == 1:
        print('Agora resta apenas uma peça no tabuleiro')
    else:
        if n == 0:
            print('Fim do jogo! O Computador ganhou!')
        else:
            print('Agora restam ', n,'peças no tabuleiro.')
    return c
def usuario_escolhe_jogada(n,m):
    print()
    num = int(input('Quantas peças você vai tirar? '))
    print()
    while 0<=num>m:
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        num = int(input('Quantas peças você vai tirar? '))
        print()
    n=n-num
    if num ==1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou', num,'peças.')
    if n ==1:
        print('Agora resta apenas uma peça no tabuleiro')
    else:
        if n == 0:
            print()
            print('Fim do jogo! O usuário ganhou!')
        else:
            print('Agora restam ', n,'peças no tabuleiro.')
    return num
def partida():
    n=int(input('Quantas peças? '))
    m=int(input('Limite de peças por jogada? '))
    if n%(m+1)!=0:
        print()
        print('Computador começa!')
        print()
        while n>0:
            n=n-computador_escolhe_jogada(n,m)
            if n>0:
                n=n-usuario_escolhe_jogada(n,m)    

    else:
        print()
        print('Você começa!')
        while n>0:
            n=n-usuario_escolhe_jogada(n,m)
            n=n-computador_escolhe_jogada(n,m)
print()
print()
print('Bem-vindo ao jogo no NIM! Escolha:')
print()
t=int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato:'))
if t == 1:
    print()
    print('Você escolheu uma partida isolada!')
    print()
    partida()
else:
    print()
    print('Você escolheu um campeonato!')
    print()
    rodada=0
    while rodada<3:
        rodada=rodada+1
        print()
        print('**** Rodada',rodada, '****')
        print()
        partida()
        print()
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você 0 X 3 Computador')
