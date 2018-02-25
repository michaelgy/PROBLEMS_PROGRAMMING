n = int(input())

def f_equal(x,y):
    lx = len(x)
    i = 0
    nt = True
    while i<lx:
        if x[i] != y[i]:
            return i
        i+=1
    return i

def get_formated(x,lg):
    return ("{:0"+str(lg)+"}").format(x)

def p_sec(f,l,lg):
    wf = get_formated(f,lg)
    wl = get_formated(l,lg)
    ind = f_equal(wf,wl)
    print(wf+"-"+str(int(wl[ind:],10)))

caso = 0
while n:
    caso +=1
    sec = False
    f = -1
    l = -1
    wa = input()
    lg = len(wa)
    a = int(wa,10)
    lprint = False
    n -= 1
    print("Case {}:".format(caso))
    while n:
        n-=1
        wb = input()
        b = int(wb,10)
        if b-a == 1:
            f = a
            l = b
            sec = True
        elif b-l == 1 and sec:
            l = b
        else:
            if sec:
                p_sec(f,l,lg)
                sec = False
                if not n:
                    print(wb)
            else:
                print(wa)
                if not n:
                    print(wb)
            wa = wb
            a = b
        if not n:
            lprint = True
            if sec:
                p_sec(f,l,lg)
                sec = False
    if not lprint:
        print(wa)
    print()
    n = int(input())
