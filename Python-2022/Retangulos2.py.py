n=int(input('Digita a largura:'))
m=int(input('Digite a altura:'))
x=1
y=1
while x<=m:
    if x==1 or x ==m:
        while y<=n:
            print('#', end = '')
            y=y+1
        x=x+1
        print()
        y=1
    else:
        while y<=n:
            if y==1 or y==n:
                print('#', end = '')
                y=y+1
            else:
                print(' ', end='')
                y=y+1
        x=x+1
        print()
        y=1