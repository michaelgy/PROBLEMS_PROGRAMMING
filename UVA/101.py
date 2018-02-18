n = int(input())
stack = [[[e],e] for e in range(n)]
def move(command):
    c = command.split()
    c[1] = int(c[1])
    c[3] = int(c[3])
    if c[1] != c[3] and stack[c[1]][1] != stack[c[3]][1]:
        if c[2] == "onto":
            tmp1 = stack[stack[c[3]][1]][0].pop()
            while tmp1!= c[3]:
                stack[tmp1][0].append(tmp1)
                stack[tmp1][1] = tmp1
                tmp1 = stack[stack[c[3]][1]][0].pop()
            stack[stack[c[3]][1]][0].append(c[3])
        if c[0] == "move":
            tmp = stack[stack[c[1]][1]][0].pop()
            while tmp!= c[1]:
                stack[tmp][0].append(tmp)
                stack[tmp][1] = tmp
                tmp = stack[stack[c[1]][1]][0].pop()
            stack[c[1]][1] = stack[c[3]][1]
            stack[stack[c[3]][1]][0].append(c[1])
        else:
            i = stack[stack[c[1]][1]][0].index(c[1])
            stack[stack[c[3]][1]][0] += stack[stack[c[1]][1]][0][i:]
            for e in stack[stack[c[1]][1]][0][i+1:]:
                stack[e][1] = stack[c[3]][1]
            stack[stack[c[1]][1]][0] = stack[stack[c[1]][1]][0][:i]
            stack[c[1]][1] = stack[c[3]][1]
command = input()
while command != "quit":
    try:
        move(command)
        command = input()
    except ValueError:
        for e in range(n):
            print(e,stack[e])
        print(command)
        break
for e in range(n):
    print("{}:".format(e),end="")
    for e in stack[e][0]:
        print(" {}".format(e),end="")
    print()
