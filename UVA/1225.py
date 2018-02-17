t = int(input())
while t:
    n = int(input())
    x = [0 for e in range(10)]
    for e in range(1,n+1):
        for i in str(e):
            x[int(i)] += 1
    for e in x[:-1]:
        print(e,end=" ")
    print(x[-1])
    t-=1
    
