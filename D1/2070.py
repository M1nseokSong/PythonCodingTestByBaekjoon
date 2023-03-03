# 큰 놈, 작은 놈, 같은 놈
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a<b:
        result = "<"
    elif a>b:
        result = ">"
    else:
        result = "="
    print("#%d %s" %(_+1, result))