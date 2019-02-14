import cmath
import time

WN = lambda a,N: cmath.exp(complex(0,-2*cmath.pi*a/N))

def direct_transform(x):
    N = len(x)
    X = [0]*N
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*WN(k*n,N)
    return X

def fft_div2(x):
    N = len(x) #n = l+mL, k = Mp+q
    if N%2 == 1:
        N+=1
        x.append(0)
    L = 2
    M = N//2
    X = [0]*N
    F = [[0]*M for i in range(L)]
    G = [[0]*M for i in range(L)]
    for l in range(L):
        for q in range(M):
            for m in range(M):
                F[l][q] += x[l+m*L]*WN(m*q,M)
    for l in range(L):
        for q in range(M):
            G[l][q] = F[l][q]*WN(l*q,N)
    for p in range(L):
        for q in range(M):
            for l in range(L):
                X[M*p+q] += G[l][q]*WN(l*p,L)
    return X

import random
x = [random.randint(0,10000) for i in range(1000)]

#TEST
start_time = time.time()
direct_transform(x)
print("--- %s seconds (DTFT) ---" % (time.time() - start_time))
start_time = time.time()
fft_div2(x)
print("--- %s seconds (FFT) ---" % (time.time() - start_time))
