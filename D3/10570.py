# D3
# 제곱 팰린드롬 수
t = int(input())
for _ in range(1, t+1):
    a, b = map(int, input().split())
    result = 0
    for i in range(a, b+1):
        mini_i = i**(0.5)
        if mini_i.is_integer() and str(i)==str(i)[::-1] and str(int(mini_i))==str(int(mini_i))[::-1]:
            result += 1
    print(f"#{_} {result}")
