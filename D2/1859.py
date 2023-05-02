t = int(input())
for _ in range(1, t+1):
    days = int(input())
    money = list(map(int, input().split()))
    cell, result = 0, 0
    for i in money[::-1]:
        if i > cell:
            cell = i
        else:
            result += cell - i
    print(f"#{_} {result}")