class FlowNetwork: 
    def __init__(self,graph): 
      # residual network
      self.graph = graph  
      self.n_node = len(graph) 
        
    def findForwardPath(self,s, t, flowPath): 
        visited =[False]*(self.n_node) 
        nodes=[] 
        nodes.append(s) 
        visited[s] = True
        while nodes: 
            u = nodes.pop(0) 
            for idx, forward in enumerate(self.graph[u]): 
                if (visited[idx] == False and forward > 0) : 
                    nodes.append(idx) 
                    visited[idx] = True
                    flowPath[idx] = u 
        if visited[t]:
          return True
        else:
          return False
              
    def FordFulkerson(self, source, sink): 
        flowPath = [-1]*(self.n_node) 
        max_flow = 0 
        while self.findForwardPath(source, sink, flowPath) : 
            forwardPath = float("Inf") 
            s = sink 
            while(s !=  source): 
              forwardPath = min (forwardPath, self.graph[flowPath[s]][s]) 
              s = flowPath[s] 
            max_flow +=  forwardPath 
            v = sink 
            while(v !=  source): 
                u = flowPath[v] 
                self.graph[u][v] -= forwardPath 
                self.graph[v][u] += forwardPath 
                v = flowPath[v] 
        return max_flow 
   
def main():
  graph = [[0, 8, 9, 5, 0], 
          [0, 0, 0, 7, 0], 
          [0, 4, 0, 0, 8], 
          [0, 0, 0 ,0, 6], 
          [0, 0, 0, 0, 0]] 
    
  network = FlowNetwork(graph) 
    
  source = 0; 
  sink = 4;
    
  print ("The maximum possible flow is %d ." % network.FordFulkerson(source, sink)) 

if __name__== "__main__":
  main()
