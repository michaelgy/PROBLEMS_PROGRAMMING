from sys import stdin
r = stdin.readline
l = r().strip()
anagrams = []
anana = []
while l != "#":
    elements = l.split()
    for e in elements:
        if len(e) == 1:
            anana.append(e)
        else:
            anag = False
            sete = [j for j in e.lower()]
            sete.sort()
            for i in anagrams:
                seti = [j for j in i.lower()]
                seti.sort()
                if seti == sete:
                    anag = True
                    break
            if not anag:
                for i in anana:
                    seti = [j for j in i.lower()]
                    seti.sort()
                    if seti == sete:
                        anana.remove(i)
                        anagrams.append(e)
                        anag = True
                if not anag:
                    anana.append(e)
    l = r().strip()
anana.sort()
for e in anana:
    print(e)