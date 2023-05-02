t = int(input())
for _ in range(1, t+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = [0] * 8
    n = int(input())
    for i in range(8):
        if n >= money[i]:
            count[i] += n // money[i]
            n %= money[i]
    print(f"#{_}")
    print(*count)