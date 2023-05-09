# D3
# 구구단2
tc = int(input())
for _ in range(1, tc+1):
    a, b = map(int, input().split())
    result = -1 if a>=10 or b>=10 else a*b
    print(f"#{_} {result}")
