from sys import stdin
import re
r = stdin.readline

def conversion(name):
    v = 0
    name = "".join(re.split("[^a-z]+",name.lower()))
    for e in name:
        v += ord(e)-ord('a')+1
    while v>=10:
        r = 0
        while v>0:
            r+=v%10
            v=v//10
        v = r
    return v

l = r().strip()
while l:
    m = r().strip()
    k1 = conversion(l)
    k2  = conversion(m)
    if k1>k2:
        print("{:.2f} %".format(k2/k1*100))
    else:
        print("{:.2f} %".format(k1/k2*100))
    l = r().strip()