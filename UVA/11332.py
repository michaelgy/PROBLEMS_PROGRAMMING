from sys import stdin
def f(n):
    s = str(n)
    suma = 0
    for e in s:
        suma += int(e)
    return suma
r = stdin.readline
n = int(r().strip())
while n!=0:
    print(f(f(f(n))))
    n = int(r().strip())
