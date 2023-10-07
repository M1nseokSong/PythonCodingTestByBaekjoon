# 단지번호붙이기
from collections import deque

def bfs(s, e):
    q = deque()
    q.append((s, e))
    v[s][e] = 1
    answer = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<n and adj[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                answer += 1
                v[ni][nj] = 1
    ans.append(answer)

n = int(input())
adj = list(list(map(int, input())) for _ in range(n))
v = list([0]*n for _ in range(n))
ans = []

for i in range(n):
    for j in range(n):
        if adj[i][j]==1 and v[i][j] == 0:
            bfs(i, j)

ans.sort()
print(len(ans))
print(*ans, sep="\n")