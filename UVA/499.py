from sys import stdin
r = stdin.readline
l = r().strip()
while l:
    letter = dict()
    for e in l.split():
        for i in e:
            if i in letter:
                letter[i] +=1
            elif i.isalpha():
                letter[i] = 1
    total = []
    for e in letter:
        total.append([e,letter[e]])
    total.sort(key = lambda x: x[0])
    total.sort(key = lambda x: x[1],reverse = True)
    m = total[0][1]
    s = ""
    for e in total:
        if e[1] == m:
            s+=e[0]
    print("{} {}".format(s,m))
    l = r().strip()