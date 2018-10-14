from sys import stdin

primes = {1,2,3,5,7,11,13,17,19,23,29,31}


r = stdin.readline
nmax = 18
used = [1]*nmax
used[0] = 0
used[0] = 1
l = [1]*nmax
def encontrar_circulo(n,total = 1):
    if total == n:
        if l[total]+1 in primes:
            for j in range(1,n):
                print(l[j],end = " ")
            print(l[n])
    else:
        for e in range(2,n+1):
            if used[e] and (l[total]+e in primes):
                used[e] = 0
                l[total+1] = e
                encontrar_circulo(n,total = total+1)
                used[e] = 1

n =r().strip()
i=0
while n:
    i+=1
    n = int(n)
    print("Case {}:".format(i))
    encontrar_circulo(n)
    n = r().strip()
    if n:
        print()
