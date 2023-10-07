# N-Queen
def dfs(i, lst):
    global result
    if i == N:
        result += 1
        return
    for k in range(N):
        if lst[k] == 0 and minus[k-i] == 0 and plus[k+i] == 0:
            lst[k] = 1
            plus[k+i] = 1
            minus[k-i] = 1
            dfs(i+1, lst)
            lst[k] = 0
            plus[k+i] = 0
            minus[k-i] = 0

N = int(input())
result = 0
lst = [0] * N
plus = [0] * (2*N)
minus = [0] * (2*N)
dfs(0, lst)
print(result)