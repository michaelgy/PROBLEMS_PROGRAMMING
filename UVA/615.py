from sys import stdin

inbuffer = []
out = []
node_count = dict()

def is_tree():
    if node_count == {}:
        return True
    rootf = None
    tree = True
    for k in node_count:
        if node_count[k][0] == 0:
            if rootf:
                tree = False
            else:
                rootf = k
        if node_count[k][0] > 1:
            tree = False
    if not rootf:
        tree = False
    if tree:
        na = [rootf]
        while na and tree:
            node = na.pop()
            if node_count[node][2] == 1:
                tree = False
            else:
                node_count[node][2] = 1
                na.extend(node_count[node][1])
    if tree:
       for k in node_count:
           if node_count[k][2] == 0:
               tree = False
    return tree

for e in stdin.readlines():
    for i in e.split():
        inbuffer.append(int(i))

f,t = inbuffer[0],inbuffer[1]
i = 2
k = 1
while t> -1:
    if f > 0:
        if f in node_count:
            node_count[f][1].append(t)
        else:
            node_count[f] = [0,[t],0]
        if t in node_count:
            node_count[t][0] +=1
        else:
            node_count[t] = [1,[],0]
    else:
        out.append( "Case {} is a tree.".format(k) if is_tree() \
                    else "Case {} is not a tree.".format(k))
        node_count.clear()
        k+=1
    
    f,t = inbuffer[i],inbuffer[i+1]
    i+=2

print("\n".join(out))

            

