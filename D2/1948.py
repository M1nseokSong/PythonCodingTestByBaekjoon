# 날짜 계산기
t = int(input())
calender = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for _ in range(t):
    m1, d1, m2, d2 = map(int,input().split())
    if m1 == m2:
        result = d2-d1+1
    else:
        result = sum(calender[m1+1:m2]) + calender[m1] - d1 + d2 + 1
    print(f"#{_+1} {result}")