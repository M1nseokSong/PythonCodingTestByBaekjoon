# 평균값 구하기
T = int(input())
for _ in range(T):
    array = list(map(int, input().split()))
    print("#%d %d" %(_+1, round(sum(array)/10)))