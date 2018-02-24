def gcd(a,b):
    c = max(a,b)
    b = min(a,b)
    k = c%b
    while k!=0:
        c = b
        b = k
        k = c%b
    return b 
data = [int(e) for e in input().split()]
i = 0
while data[0]:
    i+=1
    svalue = sum(data[1:])
    a = abs(svalue)//data[0]
    b = abs(svalue)%data[0]
    c = data[0]
    if b>1:
        k = gcd(b,c)
        b //= k
        c //= k
    print("Case {}:".format(i))
    if b<1:
        if svalue<0:
            print("- {}".format(a))
        else:
            print(a)
    else:
        db = len(str(c))
        la = len(str(a))
        avg = abs(svalue/c)
        if avg>1:
            db+=la
        if svalue<0:
            db+=2
        print(("{:>"+str(db)+"}").format(b))
        if svalue<0:
            if avg>1:
                print("- "+str(a)+"-"*(db-la-2))
            else:
                print("- "+"-"*(db-2))
        else:
            if avg>1:
                print(str(a)+"-"*(db-la))
            else:
                print("-"*db)
        print(("{:>"+str(db)+"}").format(c))
    data = [int(e) for e in input().split()]

