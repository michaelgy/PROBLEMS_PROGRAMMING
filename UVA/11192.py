l = input().split()
l[0] = int(l[0])
while l[0]:
    w = l[1]
    s = ""
    k = 0
    le = len(w)
    for e in range(l[0]):
        t = ""
        for i in range(le//l[0]):
            t=w[k]+t
            k+=1
        s+=t
    print(s)
    l = input().split()
    l[0] = int(l[0])
