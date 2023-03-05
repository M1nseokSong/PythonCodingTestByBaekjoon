# 간단한 소인수분해
T = int(input())
for _ in range(T):
    n = int(input())
    result = [0, 0, 0, 0, 0]
    array = [2, 3, 5, 7, 11]
    for i in range(5):
        while (n % array[i]) == 0:
            n = n // array[i]
            result[i] += 1
            
    print("#%d" %(_+1), ' '.join(map(str,result)))