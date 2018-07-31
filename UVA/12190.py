from sys import stdin

r = stdin.readline

def bill(n):
    if n<= 100: return 2*n
    elif n<=10000: return 200+3*(n-100)
    elif n<=1000000: return 29900+5*(n-10000)
    else: return 4979900+7*(n-1000000)

def ibill(n):
    if n<=200: return n//2
    elif n<=29900: return (n-200)//3+100
    elif n<=4979900: return (n-29900)//5+10000
    else: return (n-4979900)//7+1000000


def bisearch(fn,a,b):
    if a == b:
        return a
    if abs(a-b)== 1:
        if fn(a) == 0:
            return a
        else:
            return b
    s = a+b
    if s%2:
        s //=2
        res = fn(s)
        if res==0:
            return s
        if res<0:
            return bisearch(fn,a,s)
        else:
            return bisearch(fn,s,b)
    else:
        t = s//2
        s = t+1
        res1 = fn(t)
        res2 = fn(s)
        if abs(res2)<abs(res1):
            if res2 == 0:
                return s
            elif res2>0:
                return bisearch(fn,s,b)
            else:
                return bisearch(fn,a,t)
        elif res1 == 0:
            return t
        elif res1<0:
            return bisearch(fn,a,t)
        else:
            return bisearch(fn,s,b)

A,B = map(int,r().split())
while A+B != 0:
    ibA = ibill(A)
    fn = lambda n: bill(ibA-n)-bill(n)-B
    print(bill(bisearch(fn,0,ibA//2)))
    A,B = map(int,r().split())
