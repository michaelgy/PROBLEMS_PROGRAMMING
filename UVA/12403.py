n = int(input())
m = 0
while n>0:
    line = input()
    if(line[0] == 'd'):
        m += int(line.split()[1])
    else:
        print(m)
    n-=1
