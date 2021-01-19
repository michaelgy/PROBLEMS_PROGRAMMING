from sys import stdin
from math import ceil
r = lambda : stdin.readline().strip()



c = int(r())
for ci in range(c):
    a,b,c = map(int,r().split())
    f = False
    for i in range(1,int(ceil(b**(1/3)))+1):
        for j in range(i+1,int(ceil(b**(1/2)))+1):
            if b%(i*j) == 0:
                k = b//(i*j)
                s = i+j+k
                s1 = i-j-k
                s2 = -j-i+k
                s3 = j-i-k
                ss = i**2+j**2+k**2
                f = (s == a or s1 == a or s2 == a or s3 == a) and ss == c and \
                    i != j and i != k and j != k
                if f:
                    if s1 == a:
                        j = -j
                        k = -k
                    if s2 == a:
                        i = -i
                        j = -j
                    if s3 == a:
                        i = -i
                        k = -k
                    break
        if f:
            break
    print("{} {} {}".format(*(sorted([i,j,k]))) if f else "No solution.")
