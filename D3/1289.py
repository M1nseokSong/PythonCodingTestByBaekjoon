# 원재의 메모리 복구하기
t = int(input())
for _ in range(1, t+1):
    x = input()
    result = 0
    if x[0] == '1':
        result += 1
    for i in range(1, len(x)):
        if x[i-1] != x[i]:
            result += 1
    print(f"#{_} {result}")
