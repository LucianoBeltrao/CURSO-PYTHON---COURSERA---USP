n=int(input('Digite um número: '))
lista=[]
while n >0:
    lista.append(n)
    n=int(input('Digite um número: '))
tam = len(lista) - 1
while tam >= 0:
    print(lista[tam])
    tam = tam-1
