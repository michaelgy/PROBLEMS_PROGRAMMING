n = int(input())
k = 0
while n:
    k+=1
    st = [int(i) for i in input().split()]
    s = sum(st)
    m = 0
    prom = s//n
    for i in st:
        if i>prom:
            m+=i-prom
    print("Set #{}".format(k))
    print("The minimum number of moves is {}.".format(m))
    print()
    n = int(input())
