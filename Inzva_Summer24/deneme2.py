n = int(input())
edges = []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
nodes = [TreeNode(i) for i in range(n+1)]
for i in range(n-1):
    u, type, v = map(int, input().split())
    if type == 0:
        nodes[u].left = nodes[v]
    else:
        nodes[u].right = nodes[v]

def vertical_order_traversal(root):
    if not root:
        return []
    queue = [(root, 0, 0)]
    vertical_order =[]
    while queue:
        node, col, row = queue.pop(0)
        vertical_order.append((col,row,node.val))
        if node.left:
            queue.append((node.left, col - 1, row + 1))
        if node.right:
            queue.append((node.right, col + 1, row + 1))
    vertical_order.sort()
    vertical_order= [x[2] for x in vertical_order]
    print(*vertical_order)
vertical_order_traversal(nodes[1])