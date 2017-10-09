I = int(input())
while I>0:
    s = bin(I)[2:]
    print("The parity of %s is %d (mod 2)."%(s,s.count("1")))
    I = int(input())
