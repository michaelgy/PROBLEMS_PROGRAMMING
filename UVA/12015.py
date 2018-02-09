T = int(input())
pages = ["" for e in range(10)]
i = 0
while T>i:
    m = 0
    c = 0
    i+=1
    print("Case #{}:".format(i))
    for e in range(10):
        name,relv = [i for i in input().split()]
        relv = int(relv)
        if relv == m:
            pages[c] = name
            c+=1
        if relv >m:
            c = 1
            pages[0] = name
            m = relv
    for e in range(c):
        print(pages[e])
