from collections import defaultdict 

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance, freq):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = (distance, freq)

  def __repr__(self) -> str:
    return f'edge: {self.edges} dist: {self.d}'


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      #*
      weight = current_weight + graph.distance[(min_node, edge)][0]
      weight = (weight- (weight % graph.distance[(min_node,edge)][1]  ))
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

n, m = list(map(int, input().split()))

g = Graph()
for i in range(n):
  g.add_node(i)

for i in range(m):
  x, y, w, f = list(map(int, input().split()))
  g.add_edge(x, y, w, f)

print(dijsktra(g, initial=1))
  