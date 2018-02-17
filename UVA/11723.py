from math import ceil

n,r = [int(e) for e in input().split()]
i = 0
while n:
    i+=1
    k = ceil(n/r)
    k -= 1
    print("Case {}: ".format(i),end="")
    if k<27:
        print(k)
    else:
        print("impossible")
    n,r = [int(e) for e in input().split()]        
