T = int(input())
for _ in range(T):
    result = 0
    N = int(input())
    result = sum([i if i%2 == 1 else (-1*i) for i in range(1, N+1)])
    print("#%d %d" %(_+1, result))