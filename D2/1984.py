t = int(input())
for _ in range(1, t+1):
    number = list(map(int, input().split()))
    number.sort()
    print(f"#{_} {round(sum(number[1:-1])/8)}")