# 스타트링크
from collections import deque

def bfs():
    v = [0] * 1000001
    q = deque()
    q.append(S) # 처음 위치
    v[S] = 1

    while q:
        c = q.popleft()
        if c == G:
            return v[c] -1
        for n in (c+U, c-D):
            if 1<=n<=1000000 and v[n]==0:
                q.append(n)
                v[n] = v[c] + 1
    return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs())
