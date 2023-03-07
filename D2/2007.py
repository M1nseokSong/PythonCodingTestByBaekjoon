# 패턴 마디의 길이
T = int(input())
for _ in range(T):
    N = input()
    for i in range(1, len(N)):
        cnt = 0
        tmp = 30//i # i=5, tmp=6
        for j in range(1, tmp): #j=1,2,3,4,5
            if N[0:i] == N[j*i:(j+1)*i]:
                cnt += 1
        if cnt == tmp-1:
            print(f"#{_+1} {i}")
            break