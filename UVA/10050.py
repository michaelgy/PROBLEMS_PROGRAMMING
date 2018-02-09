t = int(input())
d = [0 for e in range(3650)]
while t>0:
    n = int(input())
    p = int(input())
    for e in range(n):
        d[e] = 0
    for e in range(p):
        k = int(input())
        h = k
        k-=1
        while k<=n:
            d[k] = 1
            k += h
    c = 0
    m = 0
    lim = 5
    while m<n:
        if d[m]:
            c+=1
        m+=1
        if m == lim:
            m+=2
            lim+=7
    print(c)
    t-=1
