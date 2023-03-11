n=int(input('Digita a largura:'))
m=int(input('Digite a altura:'))
linha=1
coluna=1
while linha<=m:
    while coluna<=n:
        print('#', end = '')
        coluna=coluna+1
    linha=linha+1
    print()
    coluna =1
    