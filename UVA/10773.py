import math
n = int(input())
i = 0
while n:
    i+=1
    d,v,u = [int(e) for e in input().split()]
    print("Case {}: ".format(i),end="")
    if v > u or v == u or v == 0:
        print("can't determine")
    else:
        t1 = d/u
        theta = math.asin(v/u)
        t2 = d/(u*math.cos(theta))
        print("{:.3f}".format(t2-t1))
    n -= 1
