from math import sqrt

from sys import stdin


"""
this is for test and precalculate
def find_all(n):
    for e in range(n):
        x = (-1+(1+8*e**2)**(1/2))/2
        if abs(x-round(x))<1e-6:
            print(e,x)


def center(c):
    sqrt2 = sqrt(2)
    return -((3-2*sqrt2)**c-(3+2*sqrt2)**c)/(4*sqrt2)

def nvalue(c):
    sqrt2 = sqrt(2)
    return 0.5*(-1+0.5*((3-2*sqrt2)**c+(3+2*sqrt2)**c))

def prueba_exp():
    for i in range(1,30):
        v=center(i)
        n = nvalue(i)
        if n>=10**15:
            return
        print(round(n),",")


"""
sset = [1 ,
        8 ,
        49 ,
        288 ,
        1681 ,
        9800 ,
        57121 ,
        332928 ,
        1940449 ,
        11309768 ,
        65918161 ,
        384199200 ,
        2239277041 ,
        13051463048 ,
        76069501249 ,
        443365544448 ,
        2584123765441 ,
        15061377048200 ,
        87784138523761 ,
        511643454094368]

lines = stdin.readlines()
for line in lines:
    n = int(line.strip())
    if n>0:
        i = 0
        k = sset[i]
        while i<len(sset)-1 and k<n:
            i+=1
            k = sset[i]
        if k>n:
            i-=1
        print(i)

