# DFS와 BFS
from collections import deque
def dfs(s):
    v[s] = 1
    result_dfs.append(s)

    for n in adj[s]:
        if not v[n]:
            dfs(n)

def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1
    result_bfs.append(s)

    while q:
        n = q.popleft()
        for e in adj[n]:
            if not v[e]:
                q.append(e)
                v[e] = 1
                result_bfs.append(e)
            


N, M, V = map(int, input().split())
adj = list([] for _ in range(N+1))
for i in range(M):
    p, q = map(int, input().split())
    adj[p].append(q)
    adj[q].append(p)
for i in range(1, N+1):
    adj[i].sort()

result_dfs = [] 
v = [0] *(N+1)
dfs(V)

result_bfs = []
v = [0] *(N+1)
bfs(V)

print(*result_dfs)
print(*result_bfs)