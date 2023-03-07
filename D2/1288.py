# 새로운 불면증 치료법
T = int(input())
for _ in range(T):
    yang = [0]*10
    N = int(input())
    tmp_N = N
    count = 1
    while True:
        for i in str(N):
            yang[int(i)] += 1
        if 0 not in yang:
            break
        N = tmp_N * count
        count += 1
    print("#%d %d" %(_+1, N))