# 암호 생성기
# D3
from collections import deque
for _ in range(10):
    n = int(input())
    flag = 0
    queue = deque(list(map(int, input().split())))
    while(True):
        for i in range(1, 6):
            tmp = queue.popleft()-i
            if tmp <= 0:
                queue.append(0)
                flag = 1
                break
            queue.append(tmp)
        if flag == 1:
            break
    print("#%d" %(_+1), end=' ')
    print(*queue)
