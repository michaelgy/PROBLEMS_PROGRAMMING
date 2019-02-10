from sys import stdin
from math import gcd

inbuffer = [[int(i) for i in e.split()] for e in stdin.readlines()]
out = []

for i in range(len(inbuffer)-1):
    s = sum(inbuffer[i][1:])
    n = inbuffer[i][0]
    i+=1
    out.append("Case {}:".format(i))
    if s%n == 0:
        if s>=0:
            out.append("{}".format(s//n))
        else:
            out.append("- {}".format(abs(s//n)))
    elif n>abs(s):
        x = gcd(s,n)
        s //= x
        n //= x
        sp = len(str(n))
        if s>=0:
            out.append(("{:>"+str(sp)+"}").format(s))
            out.append("-"*sp)
            out.append(str(n))
        else:
            out.append(("  {:>"+str(sp)+"}").format(abs(s)))
            out.append("- "+"-"*sp)
            out.append("  "+str(n))
    else:
        a = abs(s)//n*(-1 if s<0 else 1)
        s = abs(s-a*n)
        x = gcd(s,n)
        s //= x
        n //= x
        sp = len(str(n))
        asp = len(str(a))
        if a>=0:
            out.append((" "*asp+"{:>"+str(sp)+"}").format(s))
            out.append(str(a)+"-"*sp)
            out.append(" "*asp+str(n))
        else:
            out.append((" "*(asp+1)+"{:>"+str(sp)+"}").format(s))
            out.append("- "+str(abs(a))+"-"*sp)
            out.append(" "*(asp+1)+str(n))
        
        
        
print("\n".join(out))

            

