# 안전 영역
from collections import deque

def bfs():
    ans = 0
    q = deque()
    p = deque()
    for r in range(N):
        for c in range(N):
            if not v[r][c]:
                p.append((r, c))
    while p:
        pr, pc = p.popleft()
        if not v[pr][pc]:
            q.append((pr, pc))
            ans += 1
        while q:
            qr, qc = q.popleft()
            for dr, dc in((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = qr+dr, qc+dc
                if 0<=nr<N and 0<=nc<N and v[nr][nc]==0:
                    q.append((nr, nc))
                    v[nr][nc] = 1

    answer.append(ans)            
        
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
answer = [1]
for i in range(1, max(map(max, adj))+1):
    v = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if adj[r][c] <= i:
                v[r][c] = 1
    bfs()

print(max(answer))