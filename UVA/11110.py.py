from sys import stdin

r = stdin.readline
nmax = 99
mx = [[0]*nmax for i in range(nmax)]
reco = [[0]*nmax for i in range(nmax)]
sig = [[0,0] for i in range(nmax)]
init = [[0,0] for i in range(nmax)]

def inm(f,c,n):
    return f>-1 and f<n and c<n and c>-1

def vrf(npos,sigt,cval):
    if reco[npos[0]][npos[1]] == 0 and mx[npos[0]][npos[1]] == cval:
        sig[sigt][0],sig[sigt][1] = npos
        return 1
    return 0

def eqdiv(n):
    for i in range(n):
        cval = mx[init[i][0]][init[i][1]]
        isig = 0
        sig[isig][0],sig[isig][1] = init[i][0],init[i][1]
        sigt = 1
        while isig<sigt:
            pos = [sig[isig][0],sig[isig][1]]
            reco[pos[0]][pos[1]] = 1
            isig += 1
            npos = [pos[0]+1,pos[1]]
            if inm(*npos,n):
                sigt += vrf(npos,sigt,cval)
            npos = [pos[0]-1,pos[1]]
            if inm(*npos,n):
                sigt += vrf(npos,sigt,cval)
            npos = [pos[0],pos[1]+1]
            if inm(*npos,n):
                sigt += vrf(npos,sigt,cval)
            npos = [pos[0],pos[1]-1]
            if inm(*npos,n):
                sigt += vrf(npos,sigt,cval)
        if sigt<n:
            return "wrong"
    return "good"

def clear_reco(n):
    for i in range(n):
        for j in range(n):
            reco[i][j] = 0

def clear_mx(n):
    for i in range(n):
        for j in range(n):
            mx[i][j] = 0

def f_zinit(n):
    for i in range(n):
        for j in range(n):
            if mx[i][j] == 0:
                return (i,j)
    return (n-1,n-1)

def ver(n):
    for i in range(n):
        for j in range(n):
            print(mx[i][j],end=" ")
        print()
            
n = int(r().strip())
while n:
    clear_reco(n)
    clear_mx(n)
    m = 1
    while m<n:
        i = 0
        l = 0
        for k in map(int,r().split()):
            if i == 1:
                init[m][0],init[m][1] = l-1,k-1
            if i%2 == 0:
                l = k
            elif i%2 == 1:
                mx[l-1][k-1] = m
            i+=1
        m+=1
    init[0][0],init[0][1] = f_zinit(n)
    print(eqdiv(n))
    n = int(r().strip())
    
