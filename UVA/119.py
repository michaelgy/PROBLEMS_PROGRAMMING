from sys import stdin
r = stdin.readline

l = r().strip()
while l:
    n = int(l)
    flist = r().split()
    c = dict()
    for e in flist:
        c[e] = [0,0,0]
    for e in range(n):
        gl = r().strip().split()
        gl[1] = int(gl[1])
        gl[2] = int(gl[2])
        c[gl[0]][0] += gl[1]
        c[gl[0]][1] += gl[1]%gl[2] if gl[2] else gl[1]
        am = gl[1]//gl[2] if gl[2] else 0
        for i in range(gl[2]):
            c[gl[i+3]][2] += am
    for e in flist:
        print("{} {}".format(e,c[e][2]+c[e][1]-c[e][0]))
    l = r().strip()
    if l:
        print()
