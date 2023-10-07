# N과 M (1)
def dfs(n, lst):
    if n == M:
        result.append(lst)
        return result
    for i in range(1, N+1):
        if v[i] == 0:
            v[i] = 1
            dfs(n+1, lst+[i])
            v[i] = 0


N, M = map(int, input().split())
result = []
v = [0]*(N+1)
dfs(0, [])
for i in result:
    print(*i)