t = int(input())
for _ in range(1, t+1):
    a, b = map(int, input().split())
    if a+b >= 24:
        result = a+b-24
    else:
        result = a+b
    print(f"#{_} {result}")