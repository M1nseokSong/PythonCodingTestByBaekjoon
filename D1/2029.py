# 몫과 나머지 출력하기
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print("#%d %d %d" %(_+1, a//b, a%b))