# 빙산
from collections import deque

def bfs(ci, cj, v):
    q = deque()
    q.append((ci, cj))
    v[ci][cj] = 1

    while q:
        si, sj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si+di, sj+dj
            if adj[ni][nj] > 0 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1

def solve():
    for year in range(1, 100000):
        water = [[0]*M for _ in range(N)]
        for i in range(1, N-1):
            for j in range(1, M-1):
                if adj[i][j] == 0:
                    continue
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i+di, j+dj
                    if adj[ni][nj] == 0:
                        water[i][j] += 1
        for i in range(1, N-1):
            for j in range(1, M-1):
                if adj[i][j] > 0:
                    adj[i][j] = max(0, adj[i][j] - water[i][j])
        v = [[0]*M for _ in range(N)]
        cnt = 0
        for i in range(1, N-1):
            for j in range(1, M-1):
                if adj[i][j] > 0 and v[i][j] == 0:
                    bfs(i, j, v)
                    cnt += 1
                    if cnt > 1:
                        return year
        if cnt == 0:
            return 0

N, M = map(int, input().split())
adj = list(list(map(int, input().split())) for _ in range(N))
print(solve())