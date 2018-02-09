from math import sqrt
n = int(input())
P = [[0,0] for e in range(10000)]
while n:
    for e in range(n):
        P[e][0],P[e][1] = [int(e) for e in input().split()]
    dmin = 80000
    for e in range(n-1):
        for i in range(e+1,n):
            d = sqrt((P[e][0]-P[i][0])**2+(P[e][1]-P[i][1])**2)
            if d<dmin:
                dmin = d
    if dmin<10000:
        print("{:.4f}".format(dmin))
    else:
        print("INFINITY")
    n = int(input())
