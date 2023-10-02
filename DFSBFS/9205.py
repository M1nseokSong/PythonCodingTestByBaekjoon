# # 맥주 마시면서 걸어가기
# from collections import deque

# def bfs(sx, sy):
#     q = deque()
#     v = []
#     q.append((sx, sy)) # 첫 번째 편의점
#     v.append((sx, sy)) 

#     while q:
#         cx, cy = q.popleft()
#         if abs(cx-fx) + abs(cy-fy) <= 1000:
#             return "happy"
#         for s in adj: # 모든 편의점
#             if abs(cx-s[0]) + abs(cy-s[1]) <= 1000 and (s[0], s[1]) not in v:
#                 q.append((s[0], s[1]))
#                 v.append((s[0], s[1]))
#     return "sad"

# def solve():
#     store = []
#     for s in adj:
#         distance = abs(hx-s[0]) + abs(hy-s[1])
#         if distance <= 1000:
#             store.append((distance, s[0], s[1]))
#     store.sort(reverse=True, key=lambda x: x[0])
#     if abs(hx-fx) + abs(hy-fy) <= 1000:
#         return "happy" # 한번에 도착지 갈 수 있으면
#     if len(store) == 0 and abs(hx-fx) + abs(hy-fy) > 1000:
#         return "sad"
#     return bfs(store[0][1], store[0][2])


# t = int(input())
# for _ in range(t):
#     adj = []
#     n = int(input())
#     hx, hy = map(int, input().split())
#     for s in range(n):
#         x, y = map(int, input().split())
#         adj.append((x, y))
#     fx, fy = map(int, input().split())
#     print(solve())


def bfs():
    # q생성, 필요변수 등 생성
    q = []
    v = [0]*N

    # 큐에 초기데이터 삽입, si,sj는 v에 표시X
    q.append((sj,si))

    while q:
        cj,ci = q.pop(0)
        if abs(cj-ej)+abs(ci-ei)<=1000:         # 목적지 도달가능
            return 'happy'

        # 미방문 모든 편의점좌표: 범위내인지 체크
        for i in range(N):
            if v[i]==0:     # 미방문 편의점
                nj,ni = lst[i]
                if abs(cj-nj)+abs(ci-ni)<=1000: # 범위내
                    q.append((nj,ni))
                    v[i]=1

    return 'sad'

TC = int(input())
for _ in range(TC):
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj,ti))
    ej, ei = map(int, input().split())

    ans = bfs()
    print(ans)