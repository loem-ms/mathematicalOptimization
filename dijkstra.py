import numpy as np
def chooseIfromN():
  min_di = 0
  for i in N:
    if d[i-1]<=d[min_di-1]:
      min_di = i
  return min_di

def updateNS(i):
  N.remove(i)
  S.add(i)

def updateD(i):
  for idx in N:
    v = G[i-1][idx-1]
    if v>0:
      nv = d[i-1]+G[i-1][idx-1]
      if d[idx-1] > nv:
        d[idx-1] = nv
        l[idx-1] = i
    else:
      continue 

def checkRoute(s,f):
  route = []
  x = f
  while x!=s:
    route.append(l[x-1])
    x = l[x-1]
  
  route.reverse()
  route.append(f)
  return route
def main():

  G = np.array([[0,8,2,0,0,0],
                [8,0,5,4,2,0],
                [2,5,0,9,8,0],
                [0,4,9,0,1,4],
                [0,2,8,1,0,6],
                [0,0,0,4,6,0]], dtype='int')

  d = np.array([99,99,99,99,99,99],dtype='int')
  l = np.array([0,0,0,0,0,0],dtype='int')

  N = set([1,2,3,4,5,6])
  S = set()

  start = 1

  for goal in range(2,7):
    d[start-1] = 0
    while N!=set():
      i = chooseIfromN()
      updateNS(i)
      updateD(i)
      #print("i : ",i)
      #print("N : ",N)
      #print("S : ",S)
      #print("d : ",d)
      #print("l : ",l)
      #print("====================")
      if i == goal:
        break

    print("%d -> %d : %2d : "%(start,goal,d[goal-1]),checkRoute(start,goal))
    
if __name__= "__main__":
  main()
