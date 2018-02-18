import math
from sys import stdin
def cat(n):
    return math.factorial(2*n)//(math.factorial(n+1)*math.factorial(n))

cat_table = [cat(e) for e in range(11)]
r = stdin.readline
l = r().strip()
while l:
    n = int(l)
    print(cat_table[n])
    r().strip()
    l = r().strip()
    if l:
        print()


