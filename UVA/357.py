from sys import stdin
def phi_t(N,C,D):
  tab = [0 for i in range(C+1)]
  tab[0] = 1
  for i in range(N):
    for c in range(1,C+1):
      if c-D[i]>=0:
        tab[c] += tab[c-D[i]]
  return tab

D = [1,5,10,25,50]
N = 5
Cmax = 30000
t = phi_t(N,Cmax,D)
r = stdin.readline
l = r().strip()
while l:
  n = int(l)
  v = t[n]
  if v>1:
    print("There are {} ways to produce {} cents change.".format(v,n))
  else:
    print("There is only {} way to produce {} cents change.".format(1,n))
  l = r().strip()