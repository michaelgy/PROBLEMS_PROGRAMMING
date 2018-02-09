n = int(input())
names = []
for e in range(n):
    names.append(input())
song = ["Happy","birthday","to","you","Happy","birthday","to","you","Happy","birthday","to","Rujia","Happy","birthday","to","you"]
sl = 16
c = 0
while c<n:
    i = 0
    while i<sl:
        print("{}: {}".format(names[c%n],song[c%sl]))
        c+=1
        i+=1

