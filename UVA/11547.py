from sys import stdin
r = stdin.readline
t = int(r().strip())
x = lambda n: int((((n*567)/9+7492)*235)/47-498)
while t>0:
    n = int(r().strip())
    print(str(x(n))[-2])
    t-=1
