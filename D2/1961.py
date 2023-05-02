# 숫자 배열 회전
def turn(array, n):
    # 2행 0열 -> 0행 0열
    # 1행 0열 -> 0형 1열
    # 0행 0열 -> 0행 2열
    # 2행 1열 -> 1행 0열
    # 1행 1열 -> 1행 1열
    # 0행 1열 -> 1행 2열
    turn_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n-1, -1, -1):
            turn_array[i][n-1-j] = array[j][i]
    return turn_array




t = int(input())
for _ in range(t):
    n = int(input())
    array = [list(map(int, input().split())) for i in range(n)]
    array1 = turn(array, n)
    array2 = turn(array1, n)
    array3 = turn(array2, n)
    print("#%d" %(_+1))
    for i in range(n):
        print(''.join(map(str, array1[i])), end=' ')
        print(''.join(map(str, array2[i])), end=' ')
        print(''.join(map(str, array3[i])), end='\n')

        