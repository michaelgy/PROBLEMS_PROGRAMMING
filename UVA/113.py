from math import log,exp,ceil
from sys import stdin
r = stdin.readline
n = r().strip()
eps = 1e-6
while n!="":
    n = int(n)
    p = int(r().strip())
    try:
        sol = exp(log(p)/n)
        
        csol = ceil(sol)
        if csol-sol<eps:
            print(csol)
        else:
            print(round(sol))
    except ValueError:
        print(p)
    n = r().strip()
