# 두 개의 숫자열
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) > len(B):
        A, B = B, A
    result = []
    for i in range(len(B)-len(A)+1):
        sum_num = 0
        for j in range(len(A)):
            sum_num += A[j]*B[i+j]
        result.append(sum_num)
    print("#%d %d" %(_+1, max(result)))