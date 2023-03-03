# 최대수 구하기
T = int(input())
for _ in range(T):
    array = list(map(int, input().split()))
    max_array = max(array)
    print("#%d %d" %(_+1,max_array))