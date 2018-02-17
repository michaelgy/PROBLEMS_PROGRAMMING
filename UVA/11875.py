t = int(input())
i = 0
while t:
    i+=1
    t-=1
    g = [int(e) for e in input().split()]
    p = (g[0] - g[0]%2)//2+1
    print("Case {}: {}".format(i,g[p]))
