from sys import stdin
from collections import deque

r = stdin.readline
nmax = 27
wake = 0
connect = [0]*nmax
inqueue = [0]*nmax
lookat = [-1]*nmax
queue = deque()
wk = []

def awakening(N,awake):
    global wake
    t = 0
    while queue and awake<N:
        while queue:
            u = queue.popleft()
            inqueue[u] = 0
            c = 0
            i = 0
            while i<awake and c<3:
                if connect[u] & (1<<lookat[i]):
                    c+=1
                if c==3:
                    wk.append(u)
                i+=1
        if wk:
            t+=1
        for e in wk:
            wake |= 1<< e
            lookat[awake] = e
            awake+=1
        while wk:
            u = wk.pop()
            for i in range(nmax):
                if (connect[u] & (1<<i)) and (not inqueue[i]) and (not (wake & (1<<i))):
                    queue.append(i)
                    inqueue[i] = 1
    if awake<N:
        return -1
    return t

def clean():
    global wake
    wake = 0
    for i in range(nmax):
        connect[i] = 0
        lookat[i] = -1

l = r().strip()
while l:
    N = int(l)
    M = int(r().strip())
    awake = 0
    clean()
    for e in r().strip():
        ci = ord(e)-ord('A')
        lookat[awake] = ci
        wake |= 1<< ci
        awake+=1
    for e in range(M):
        x,y = r().strip()
        cx,cy = ord(x)-ord('A'),ord(y)-ord('A')
        connect[cx] |= 1<<cy
        connect[cy] |= 1<<cx
        if (wake & (1<<cx)):
            if (not (wake & (1<<cy)) )and (not inqueue[cy]):
                queue.append(cy)
                inqueue[cy] = 1
        elif (wake & (1<<cy)):
            if (not (wake & (1<<cx))) and (not inqueue[cx]):
                queue.append(cx)
                inqueue[cx] = 1
                
    t = awakening(N,awake)
    if t>-1:
        print("WAKE UP IN, {}, YEARS".format(t))
    else:
        print("THIS BRAIN NEVER WAKES UP")
    r()
    l = r().strip()
