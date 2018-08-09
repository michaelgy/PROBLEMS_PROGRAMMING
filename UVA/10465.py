from sys import stdin

def burguers(n,m,t):
    a = min(n,m)
    m = max(n,m)
    n = a
    a = t//n
    b = 1
    s = a*n
    tot = a+b-1
    while s != t and a>0:
        a-=1
        stemp = n*a+m*b
        totemp = a+b
        if stemp<=t:
            if stemp>s: 
                s = stemp
                tot = totemp
            b+=1
    return (tot,t-s)


r = stdin.readline

l = r().strip()
while l:
    n,m,t = map(int,l.split())
    b,s = burguers(n,m,t)
    print(b,s) if s else print(b)
    l = r().strip()
