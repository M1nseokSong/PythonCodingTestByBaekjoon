# 파리 퇴치
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for i in range(n)]
    result = 0
    for col in range(n-m+1):
        for row in range(n-m+1):
            pari_sum = 0
            for i in range(m):
                for j in range(m):
                    pari_sum += array[col+i][row+j]
            if pari_sum > result:
                result = pari_sum
    print(f"#{_+1} {result}")