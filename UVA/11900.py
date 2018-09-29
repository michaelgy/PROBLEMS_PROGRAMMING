from sys import stdin

r = stdin.readline

T = int(r().strip())
i = 0
while i<T:
    i+=1
    n,P,Q = map(int,r().split())
    j,p,q = 0,0,0
    t = 0
    eggs = map(int, r().split())
    while j<n and p<=P and q<=Q:
        e = eggs.__next__()
        p+=1
        q+=e
        if p<=P and q<=Q:
            t+=1
        j+=1
    print("Case {}: {}".format(i,t))
    
