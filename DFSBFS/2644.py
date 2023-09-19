# 촌수계산
from collections import deque
def bfs(s, e):
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        if c == e:
            return v[c] -1
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] = v[c] + 1
    return -1
                


n = int(input())
s, e = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    p, q = map(int, input().split())
    adj[q].append(p)
    adj[p].append(q)

print(bfs(s, e))