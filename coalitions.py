from sys import stdin
r = stdin.readline

M = 10000
t = 101
sthP = [0]*t

def coal(i,pl,n):
    if pl == M:
        return 0
    if pl<5000:
        return sthP[0]/(M-pl)
    if i == n:
        return 0
    return max(coal(i+1,pl,n),coal(i+1,pl-sthP[i],n))

tab = [[-1]*t for i in range(M)]

def coal_t(i,pl,n):
    if pl == M:
        return 0
    if pl<5000:
        return sthP[0]/(M-pl)
    if i == n:
        return 0
    if tab[pl][i] != -1:
        return tab[pl][i]
    
    ans = max(coal_t(i+1,pl,n),coal_t(i+1,pl-sthP[i],n))
    tab[pl][i] = ans
    return ans

def clean(n):
    for i in range(n):
        for j in range(M):
            tab[j][i] = -1

n,x = map(int,r().split())
while n!=0:
    c = 1
    clean(n)
    for e in range(n):
        l,ri = map(int,r().split("."))
        v = l*100+ri
        if e+1 == x:
            sthP[0] = v
        else:
            sthP[c] = v
            c+=1
    result = int(coal_t(1,M-sthP[0],n)*100000)
    if result%10 == 5:
        result += 1
    
    print("{:.2f}".format(result/1000))
    n,x = map(int,r().split())
