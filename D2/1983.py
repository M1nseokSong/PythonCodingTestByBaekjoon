t = int(input())
result = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
for _ in range(1, t+1):
    n, k = map(int, input().split())
    score = [list(map(int, input().split())) for i in range(n)]
    rank = []
    for i in range(n):
        sum_score = score[i][0] * 0.35 + score[i][1] * 0.45 + score[i][2] * 0.20
        rank.append([i+1, sum_score])
    rank.sort(reverse=True, key = lambda x : x[1])
    for i in range(n):
        if rank[i][0] == k:
            hakjum = result[i//(n//10)]
            break
    print(f"#{_} {hakjum}")