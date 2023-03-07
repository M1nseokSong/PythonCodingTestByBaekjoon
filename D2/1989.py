# 초심자의 회문 검사
T = int(input())
for _ in range(1, T+1):
    N = input()
    for i in range(len(N)//2):
        if N[i] != N[-1-i]:
            result = 0
            break
        else:
            result = 1
    print(f"#{_} {result}")