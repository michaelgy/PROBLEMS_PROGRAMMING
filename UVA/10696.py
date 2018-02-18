N = int(input())
def Fn(k):
    if k>=101:
        return k-10
    else:
        return 91
while N>0:
    T = Fn(N)
    print("f91({}) = {}".format(N,T))
    N = int(input())
    
