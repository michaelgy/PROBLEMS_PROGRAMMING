convt = {"V":"0","U":"1","C":"2","D":"3",
         "0":"V","1":"U","2":"C","3":"D"}

def flipbase(x):
    return "".join([convt[e] for e in x])
def base4(x):
    if(x == 0):
        return "0"
    y =""
    while x>0:
        y = str(x%4)+y
        x = (x-x%4)//4
    return y
        
def sumcow(x,y):
    return flipbase(base4(int(flipbase(x),4)+int(flipbase(y),4)))

def r(x):
    return "V"+x[:-1]
def l(x):
    if len(x)==8:
        return x[1:]+"V"
    return x+"V"

def norm(x):
    l = len(x)
    return x if l>=8 else ((8-l)*"V")+x

t = int(input())
print("COWCULATIONS OUTPUT")
while t:
    x = input()
    y = input()
    for e in range(3):
        op = input()
        if op == "A":
            y = sumcow(x,y)
        elif op == "R":
            y = r(y)
        elif op == "L":
            y = l(y)
    z = input()
    y = norm(y)
    print("YES" if z == y else "NO")
    t-=1
print("END OF OUTPUT")

