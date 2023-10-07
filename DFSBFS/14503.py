#로봇 청소기
def solve(ci, cj, d):
    global result
    if adj[ci][cj] == 0:
        adj[ci][cj] = 2
        result += 1
    if adj[ci-1][cj] != 0 and adj[ci+1][cj] != 0 and adj[ci][cj-1] != 0 and adj[ci][cj+1] != 0:
        if adj[ci+move[d][0]*(-1)][cj+move[d][1]*(-1)] != 1:
            solve(ci+move[d][0]*(-1), cj+move[d][1]*(-1), d)
        else:
            return result
    else:
        if d == 0:
            d = 3
        else:
            d -= 1
        if adj[ci+move[d][0]][cj+move[d][1]] == 0:
            ni, nj = ci+move[d][0], cj+move[d][1]
            solve(ni, nj, d)
        else:
            solve(ci, cj, d)
    
N, M = map(int, input().split())
si, sj, d = map(int, input().split())
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
adj = list(list(map(int, input().split())) for _ in range(N))
solve(si, sj, d)
print(result)