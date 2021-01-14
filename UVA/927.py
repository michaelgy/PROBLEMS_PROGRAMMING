from sys import stdin
from math import ceil

r = lambda : stdin.readline().strip()

t = int(r())
for i in range(t):
    a = list(map(int, r().split()))
    a = a[1:]
    d = int(r())
    k = int(r())
    n = int(ceil(((8*k/d+1)**0.5-1)/2))
    print(sum(c*n**i for i,c in enumerate(a)))
