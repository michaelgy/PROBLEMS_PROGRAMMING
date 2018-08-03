from sys import stdin

r = stdin.readline

N = int(1e6)
dk = [0]*(N+1)
dk[1] = 1
for i in range(2,N+1):
    if dk[i] == 0:
        dk[i] = 1
        for j in range(i**2,N+1,i):
            dk[j] = i

nod = [0]*(N+1)
nod[1]=1
for i in range(2,N+1):
    if dk[i] == 1:
        nod[i] = 2
    else:
        s = 0
        k = i
        while k%dk[i]==0:
            s+=1
            k//=dk[i]
        nod[i] = (s+1)*nod[k]

Ni = [1]*(64726)
i = 1
lNi = 0
k=1
while k<N:
    k=Ni[i-1]+nod[Ni[i-1]]
    Ni[i]=k
    i+=1
    
lNi = i
def bsearch(k,A,a,b):
    if A[a] == k:
        return a
    if A[b] == k:
        return b
    if a==b:
        return a
    if b-a==1:
        return a if abs(A[a]-k)<=abs(A[b]-k) else b
    m = (a+b)//2
    if A[m] == k:
        return m
    elif A[m]<k:
        return bsearch(k,A,m,b)
    else:
        return bsearch(k,A,a,m)

def fill():
    i = 0
    j = 0
    c = 0
    while j<N+1:
        if i<lNi:
            if Ni[i]==j:
                i+=1
                c+=1
        dk[j] = c
        j+=1

fill()

n = int(r().strip())
c = 0
"""
#Codigo menos optimo
while n>c:
    c+=1
    x,y = map(int,r().split())
    a,b = bsearch(x,Ni,0,lNi-1),bsearch(y,Ni,0,lNi-1)
    if Ni[a]<x: a=a+1
    if Ni[b]>y: b=b-1
    print("Case {}: {}".format(c,b-a+1))

"""

while n>c:
    c+=1
    x,y = map(int,r().split())
    print("Case {}: {}".format(c,dk[y]-dk[x-1]))
