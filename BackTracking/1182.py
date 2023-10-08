# 부분수열의 합
def dfs(n, sm, cnt):
    global result
    if n == N:
        if sm == S and cnt > 0:
            result += 1
        return
    dfs(n+1, sm+adj[n], cnt+1)
    dfs(n+1, sm, cnt)

N, S = map(int, input().split())
adj = list(map(int, input().split()))
result = 0
dfs(0, 0, 0)
print(result)