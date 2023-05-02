# 숫자를 정렬하자
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    print(f"#{_+1} {' '.join(map(str, array))}")
