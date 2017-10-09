def main():
    try:
        while(True):
            INTSIZE = 2**31 -1
            DIGITS = 10
            n1,operan,n2 = input().split()
            k1 = len(n1)
            k2 = len(n2)
            cn1 = False
            cn2 = False
            c1 = False
            c2 = False
            c3 = False
            if(not n1[0].isdigit()):
                k1 -= 1
            if(not n2[0].isdigit()):
                k2 -= 1
            if(k1 > DIGITS):
                c1 = True
            elif(k1 == DIGITS):
                cn1 = int(n1)
                if(abs(cn1) > INTSIZE):
                    c1 = True
            if(k2 > DIGITS):
                c2 = True
            elif(k2 == 5):
                cn2 = int(n2)
                if(abs(cn2) > INTSIZE):
                   c2 = True
            if(c1):
                 print("first number too big")
            if(c2):
                 print("second number too big")
            
            if((c1 or c2) and (n1[0] == n2[0]) and (operan == "+")):
                c3 = True
            else:
                if(isinstance(cn1,bool)):
                    cn1 = int(n1)
                if(isinstance(cn2,bool)):
                    cn2 = int(n2)
                if(operan == "+"):
                    cn3 = cn1+cn2
                else:
                    cn3 = cn1*cn2
                if(abs(cn3) > INTSIZE):
                    c3 = True
            if(c3):
                print("result too big")
    except EOFError:
                pass
main()
