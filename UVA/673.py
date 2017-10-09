from sys import stdin
r = stdin.readline
n = int(r().strip())
while n>0:
    n-=1
    s = r().strip()
    ls = len(s)
    if ls%2 == 1:
        print("No")
    else:
        pb = []
        j = 0
        i = -1
        for i in range(ls):
            if s[i] == '(' or s[i] == '[':
                pb.append(s[i])
                j+=1
            elif s[i] == ')' and j>0:
                if pb[j-1] == '(':
                    pb.pop()
                    j-=1
                else:
                    break
            elif s[i] == ']' and j>0:
                if pb[j-1] == '[' :
                    pb.pop()
                    j-=1
                else:
                    break
            else:
                break
        if pb == [] and i==ls-1 and j==0:
            print("Yes")
        else:
            print("No")
    
