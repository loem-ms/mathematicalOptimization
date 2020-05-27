import numpy as np

class dijkstra:
    def __init__(self,G):
        self.G = G
        self._d_G = len(G);
        self._d = [float("inf")]*self._d_G
        self._l = [0]*self._d_G

        self._N = set([x+1 for x in range(self._d_G)])
        self._S = set()

    def _chooseIfromN(self):
        min_di = 0
        for i in self._N:
            if self._d[i-1]<=self._d[min_di-1]:
                min_di = i
        return min_di
    
    def _updateNS(self,i):
        self._N.remove(i)
        self._S.add(i)

    def _updateD(self,i):
        for idx in self._N:
            v = self.G[i-1][idx-1]
            if v>0:
                nv = self._d[i-1]+self.G[i-1][idx-1]
                if self._d[idx-1] > nv:
                    self._d[idx-1] = nv
                    self._l[idx-1] = i
                else:
                    continue 

    def checkRoute(self,s,f):
        route = []
        x = f
        while x!=s:
            route.append(self._l[x-1])
            x = self._l[x-1]
        
        route.reverse()
        route.append(f)
        return route
    
    def printRoute(self,s,f):
        print("node%d -> node%d : shortest-length: %2d ; path: "%(s,f,self._d[f-1]),self.checkRoute(s,f))

    def solve(self,start,goal):
        print("==============================")
        print("Solving for : Start at node%d, Goal at node%d"%(start,goal))
        print("==============================")
        self._d[start-1] = 0
        while self._N!=set():
            i = self._chooseIfromN()
            self._updateNS(i)
            self._updateD(i)
            print("remove node%d from N and insert into S"%i)
            print("̤N : "+str(self._N))
            print("S : "+str(self._S))
            print("d : "+str(self._d))
            print("l : "+str(self._l))
            print("==============================")
            if i == goal:
                break


def main():
    G = [[0,8,2,0,0,0],
        [8,0,5,4,2,0],
        [2,5,0,9,8,0],
        [0,4,9,0,1,4],
        [0,2,8,1,0,6],
        [0,0,0,4,6,0]]

    solver = dijkstra(G)
    start = 1
    goal  = 6
    solver.solve(start,goal)
    solver.printRoute(start,goal)

if __name__== "__main__":
    main()
