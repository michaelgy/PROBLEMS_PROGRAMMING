from bisect import bisect, bisect_left
x = [3,5,7,11,13,17,31,37,71,73,79,97,113,131,197,199,311,337,373,719,733,919,971,991,1193,1931,3119,3779,7793,7937,9311,9377,11939,19391,19937,37199,39119,71993,91193,93719,93911,99371,193939,199933,319993,331999,391939,393919,919393,933199,939193,939391,993319,999331]
lr = [int(e) for e in input().split()]
while len(lr)>1:
    left = bisect_left(x,lr[0])
    rigth = bisect(x,lr[1])
    k = rigth-left
    if k>1:
        print("{} Circular Primes.".format(k))
    elif k==1:
        print("1 Circular Prime.")
    else:
        print("No Circular Primes.")
    lr = [int(e) for e in input().split()]
