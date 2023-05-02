t = int(input())
for _ in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    m = m1 + m2
    h = h1 + h2 + m//60
    m%=60
    if h >= 13:
        h-=12
    print(f"#{_} {h} {m}")