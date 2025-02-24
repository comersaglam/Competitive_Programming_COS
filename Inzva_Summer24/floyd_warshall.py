 #* all nodes to all nodes in n^3 time complexity
#* can be used when there are negative weights
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=[[10001 for _ in range(n)] for _ in range(n)]
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        dist=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i].append(graph[i][j])
        
        for k in range(n): # Intermediate nodes
            for i in range(n): # Starting node
                for j in range(n): # Ending node
                    x=dist[i][k]+dist[k][j]
                    if x<dist[i][j]:
                        dist[i][j]=x
        resultNode=-1
        numCity=n
        for i in range(n):
            curNumCity=0
            for j in range(n):
                if i!=j and dist[i][j] <= distanceThreshold:
                    curNumCity+=1
            if curNumCity<=numCity:
                resultNode=i
                numCity=curNumCity
        return resultNode
                           