from sys import stdin

r = stdin.readline

def sm2(a,b):
    return (a^b)&1

def sumr(m):
    fg = []
    for i in range(3):
        r = []
        for j in range(3):
            s = 0
            #s = m[i][j]
            if i-1>-1:
                s = sm2(s,m[i-1][j])
            if j+1<3:
                s = sm2(s,m[i][j+1])
            if i+1<3:
                s = sm2(s,m[i+1][j])
            if j-1>-1:
                s = sm2(s,m[i][j-1])
            r.append(s)
        fg.append(tuple(r))
    return tuple(fg)

def conv2(m):
    return int("".join(["".join(map(str,x)) for x in m]),base=2)

def sol(m):
    sec = dict()
    i = 0
    while m not in sec:
        sec[m] = i
        m = sumr(m)
        i+=1
    #print(sec)
    return sec[m]-1
    
    """
    i = ""
    while not i:
        for i in fg:
            for d in i:
                print(d,end="")
            print()
        fg = sumr(fg)
        i = input()
    
    return 0
    """

n = int(r().strip())
out = []
while n:
    r()
    m = tuple(tuple(int(x) for x in r().strip()) for i in range(3))
    out.append(str(sol(m)))
    n-=1

print("\n".join(out))
