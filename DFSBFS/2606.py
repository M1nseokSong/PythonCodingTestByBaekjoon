# 바이러스
from collections import deque

def bfs(s):
    global ans
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] = 1
                ans += 1
    return ans

def dfs(s):
    global ans
    v[s] = 1
    ans += 1
    
    for n in adj[s]:
        if not v[n]:
            dfs(n)
    return ans - 1
    

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
v = [0] * (n+1)
ans = 0
for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)
print(dfs(1))