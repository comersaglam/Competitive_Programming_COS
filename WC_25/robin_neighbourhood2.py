from collections import deque

n = int(input())
cost = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

heights = [0]*n

dp0 = [0]*n # if you dont take the current node
dp1 = [0]*n # if you take the current node
visited = [False]*n


def dfs(node, parent=None):
    visited[node] = True

    take = cost[node]
    dont_take = 0

    for child in tree[node]:
        if not visited[child]:
            dfs(child)

            for grandchild in tree[child]:
                if not visited[grandchild]:
                    dfs(grandchild)

                    take += dp0[child]
                    dont_take += max(dp0[grandchild], dp1[grandchild])
                else:
                    take += dp0[child]
                    dont_take += dp0[grandchild]

    dp0[node] = dont_take
    dp1[node] = take

dfs(0)
print(max(dp0[0], dp1[0]))