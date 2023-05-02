# 파스칼 삼각형

# t = int(input())
# for _ in range(1, t+1):
#     pascal = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], 
#             [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
#     n = int(input())
#     print(f"#{_}")
#     for i in range(n):
#         if i == 0 or i == 1:
#             print(*pascal[i])
#         else:
#             for j in range(1, i):
#                 pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#             print(*pascal[i])

t = int(input())
for _ in range(1, t+1):
    pascal = []
    n = int(input())
    print(f"#{_}")
    for i in range(n):
        tmp = []
        for j in range(0, i+1):
            if j==0 or j==i:
                tmp.append(1)
            else: 
                tmp.append(pascal[i-1][j-1] + pascal[i-1][j])
        pascal.append(tmp)
    for i in pascal:
        print(*i)