from sys import stdin
from collections import deque

r = stdin.readline
nmax = 26
wake = [0]*nmax
connect = [0]*nmax
inqueue = [0]*nmax
lookat = [-1]*nmax
queue = deque()


def awakening(N,awake):
    t = 0
    while queue and awake<N:
        u = queue.popleft()
        inqueue[u] = 0
        c = 0
        i = 0
        while i<awake and c<3:
            if connect[u] & 1<<lookat[i]:
                c+=1
            if c==3:
                awake+=1
                
