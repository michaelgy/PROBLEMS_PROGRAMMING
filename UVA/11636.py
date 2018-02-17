from math import log2

n = int(input())
i=0
while n>0:
    i+=1
    k = log2(n)
    k = int(k) if k.is_integer() else int(k)+1
    print("Case {}: {}".format(i,k))
    n = int(input())
