from sys import stdin
r = stdin.readline
nd = 21
denom = [i**3 for i in range(1,nd+1)]
INF = float('inf')
M = 10000
tws = [[0]*nd for i in range(M)]

for e in range(nd):
    tws[0][e] = 1
    tws[1][e] = 1

for e in range(M):
    tws[e][0] = 1

def totalways(n,di):
    if n == 0:
        return 1
    if di < 0:
        return 0
    if n<denom[di]:
        return totalways(n,di-1)
    else:
        return totalways(n,di-1)+totalways(n-denom[di],di)

def totalways_tab(n,di):
    ni,i = 2,1
    while ni<=n:
        #print(ni,i)
        if i == di:
            ni,i = ni+1,0
        else:
            if ni<denom[i]:
                #print("entro1",tws[ni][i-1],ni,i)
                tws[ni][i] = tws[ni][i-1]
            else:
                #print("entro2")
                tws[ni][i] = tws[ni-denom[i]][i]+tws[ni][i-1]
        i+=1
    return tws[n][di-1]

totalways_tab(9999,nd)
l = r().strip()
while l:
    n = int(l)
    print(tws[n][nd-1])
    l = r().strip()
