t = int(input())
for _ in range(1, t+1):
    alpha = input()
    mo = "aioue"
    result = ""
    for i in alpha:
        if i not in mo:
            result += i
    print(f"#{_} {result}")