class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 

    def find(self, parent, i): 
        if parent[i] != i: 
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 

    def union(self, parent, rank, x, y): 
        xr = self.find(parent, x) 
        yr = self.find(parent, y) 
        if rank[xr] < rank[yr]: 
            parent[xr] = yr 
        elif rank[xr] > rank[yr]: 
            parent[yr] = xr 
        else: 
            parent[yr] = xr 
            rank[xr] += 1

    def KruskalMST(self): 
        result = [] 
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2]) 
        parent = [] 
        rank = [] 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
        while e < self.V - 1: 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 

        # Calculate maximum score
        mst_edges = set((u, v, w) for u, v, w in result)
        max_score = sum(w for u, v, w in self.graph if w > 0 and (u, v, w) not in mst_edges)

        return max_score

# Driver code 
if __name__ == '__main__': 
    n, m = map(int, input().split())
    g = Graph(n) 

    for _ in range(m):
        u, v, w = map(int, input().split())
        g.addEdge(u - 1, v - 1, w)

    score = g.KruskalMST()
    print(score)
