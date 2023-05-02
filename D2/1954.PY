# 달팽이 숫자
t = int(input())
turn = [[0, 1], [1, 0], [0, -1] , [-1, 0]] * 30
for _ in range(t):
    row, column = 0, -1
    start = 0
    n = int(input())
    array = [[0]*n for i in range(n)]
    for i in range(2*n-1):
        while(True):
            if row+turn[i][0] >= n or column+turn[i][1] >= n:
                break
            else:
                row += turn[i][0]
                column += turn[i][1]
                start += 1
            if array[row][column] == 0:
                array[row][column] = start
            else:
                row -= turn[i][0]
                column -= turn[i][1]
                start -=1
                break

            
    print("#%d" %(_+1))
    for i in range(n):
        print(' '.join(map(str, array[i])))







# 열 +1, 행 +1, 열 -1, 행 -1