# N과 M (2)
def dfs(i, k, lst):
    if i == M:
        result.append(lst)
        return
    for j in range(k+1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(i+1, j, lst+[j])
            v[j] = 0


N, M = map(int, input().split())
v = [0] * (N+1)
result = []
dfs(0, 0, [])
for i in result:
    print(*i)
