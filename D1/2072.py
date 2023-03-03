# 홀수만 더하기
T = int(input())
for _ in range(T):
    result = 0
    array = list(map(int, input().split()))
    # for i in range(len(array)):
    #     if array[i] % 2 == 1:
    #         result += array[i]
    result = sum([array[i] for i in range(len(array)) if array[i]%2==1])
    print("#%d %d" %(_+1, result))
    