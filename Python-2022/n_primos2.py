def n_primos(n):
    c=0
    while n>=1:
        y=2
        while n%y!=0 and y<n/2:
            y=y+1
        if n%y == 0:
            c=c+0
        else:
            c=c+1
        n=n-1 
    print(c)

n_primos(7)