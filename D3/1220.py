# for _ in range(1, 11):
#     n = int(input())
#     result = 0
#     magnetic = [list(map(int, input().split())) for i in range(100)]
#     for col in range(100):
#         for row in range(1, 100):
#             counting = 0
#             if magnetic[row][col] == 2: 
#                 for up in range(row-1, -1, -1):
#                     if magnetic[up][col] == 0:
#                         counting += 1
#                     elif magnetic[up][col] in (1, 2):
#                         break
#                 magnetic[row][col] = 0
#                 magnetic[row-counting][col] = 2
    
#     for col in range(100):
#         for row in range(99):    
#             if magnetic[row][col] == 1 and magnetic[row+1][col] == 2:
#                 result += 1
#     print(f"#{_} {result}")

for _ in range(1, 11):
    n = int(input())
    result = 0
    magnetic = [list(map(int, input().split())) for i in range(100)]
    for col in range(100):
        flag = 0
        for row in range(100):
            if magnetic[row][col] == 1:
                flag = 1
            elif magnetic[row][col] == 2 and flag == 1:
                result += 1
                flag = 0
    print(f"#{_} {result}")
