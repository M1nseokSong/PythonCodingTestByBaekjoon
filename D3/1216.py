# 회문2
def Recursive(array):
    for i in range(100, 0, -1): # 최대 100칸부터 시작
        for j in range(0, 100-i+1): # 시작할 수 있는 start 지점
            for row in range(100): # 첫 행부터
                if array[row][j:j+i] == array[row][j:j+i][::-1]:
                    return i
                # for k in range(i//2):
                #     if array[row][j+k] != array[row][j+i-1-k]:
                #         break
                # else:
                #     return i
                
for tc in range(1, 11):
    T = int(input())
    array = list(input() for _ in range(100))
    turn_array = list(map(list, zip(*array[::-1])))
    result = max(Recursive(array), Recursive(turn_array))
    print(f"#{tc} {result}")