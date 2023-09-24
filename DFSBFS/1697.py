# 숨바꼭질
from collections import deque

def bfs(N, K):
    v = [0] * 100001
    q = deque()
    q.append(N)
    v[N] = 1

    while q:
        c = q.popleft()
        if c == K:
            return v[c] -1
        for d in (-1, 1, c):
            n = c+d
            if 0<=n<=100000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

N, K = map(int, input().split())
print(bfs(N, K))