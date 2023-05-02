# 가랏! RC카!
t = int(input())
for _ in range(t):
    n = int(input())
    speed = 0
    result = 0
    for i in range(n):
        array = list(map(int,input().split()))
    
        if array[0] == 1:
            speed += array[1]
        elif array[0] == 2:
            if array[1] > speed:
                speed = 0
            else:
                speed -= array[1]
        result += speed
        
    print(f"#{_+1} {result}")