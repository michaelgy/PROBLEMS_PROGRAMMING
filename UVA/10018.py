from sys import stdin
r = stdin.readline
n = int(r().strip())
while n>0:
    n-=1
    snum = r().strip()
    num = int(snum)
    l = len(snum)
    c = 0
    while snum[-1:-l-1:-1] != snum:
        num += int(snum[-1:-l-1:-1])
        snum = str(num)
        l = len(snum)
        c+=1
    print("{} {}".format(c,snum))

