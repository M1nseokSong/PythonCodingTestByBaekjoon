#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 1
    box_range = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    box_a = [0, 1, 2] * 3
    box_b = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    sdoku = [1]*10
    puzzle = [list(map(int, input().split())) for i in range(9)]
    for i in range(9):
        my_sdoku_row = [1] + [0]*9
        my_sdoku_col = [1] + [0]*9
        for j in range(9):
            my_sdoku_row[puzzle[i][j]] += 1
            my_sdoku_col[puzzle[j][i]] += 1
        if sdoku != my_sdoku_row or sdoku != my_sdoku_col:
            result = 0
            break
    for j in range(9):
        my_sdoku_box = [1] + [0]*9
        for k in range(9):
            my_sdoku_box[puzzle[box_b[k]+box_range[j]][box_range[j]+box_a[k]]] +=1
        if sdoku != my_sdoku_box:
            result = 0
            break
    print(f"#{test_case} {result}")