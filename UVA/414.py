N = int(input())
spaces = [0 for e in range(13)]
while N:
    for i in range(N):
        spaces[i] = input().count(' ')
    c = 0
    k = min(spaces[:N])
    for i in range(N):
        c+=spaces[i]-k
    print(c)
    N = int(input())
