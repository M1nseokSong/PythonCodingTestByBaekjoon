# 토마토
from collections import deque

def bfs():
    q = deque()
    cnt = 0 # 안익은 개수
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if adj[h][i][j] == 1:
                    q.append((h, i, j))
                    v[h][i][j] = 1
                elif adj[h][i][j] == 0:
                    cnt += 1
    while q:
        ch, ci, cj = q.popleft()
        for dh, di, dj in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0 ,0, -1), (0, 0, 1)):
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and adj[nh][ni][nj] == 0 and v[nh][ni][nj] == 0:
                q.append((nh, ni, nj))
                cnt -= 1
                v[nh][ni][nj] = v[ch][ci][cj] + 1
    if cnt == 0:
        return v[ch][ci][cj] -1
    else:
        return -1

M, N, H = map(int, input().split())
adj = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]
v = [[[0]*M for i in range(N)] for j in range(H)]
print(bfs())