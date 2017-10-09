from sys import stdin

l = stdin.readline().strip()
i = 1
while l != "":
    c,s = map(int, l.split())
    sp = [int(e) for e in stdin.readline().strip().split()]
    am = sum(sp)/c
    for e in range(c*2-s):
        sp.append(0)
    sp.sort()
    print("Set #{}".format(i))
    im = 0
    for e in range(c):
        s = ""
        im += abs(sp[e]+sp[-(1+e)]-am)
        if sp[e] != 0:
            s+= " "+str(sp[e])
        s += " "+str(sp[-(1+e)])
        print(" {}:{}".format(e,s))
    print("IMBALANCE = {:.5f}\n".format(im))
    i+=1
    l = stdin.readline().strip()