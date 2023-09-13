from collections import deque
def bfs(r, c):
    q = deque()
    q.append((0, 0))
    v[0][0] = 1

    while q:
        cx, cy = q.popleft()
        if (cx, cy) == (r, c):
            return v[r][c]
        for i in ((-1,0), (0,-1), (1,0), (0,1)):
            nx, ny = cx + i[0], cy + i[1]
            if 0<=nx<N and 0<=ny<M and v[nx][ny] == 0 and adj[nx][ny] == 1:
                    q.append((nx, ny))
                    v[nx][ny] = v[cx][cy] + 1

N, M = map(int, input().split())
adj = list(list(map(int, input()))for _ in range(N))
v = list([0]*M for _ in range(N))
print(bfs(N-1, M-1))
