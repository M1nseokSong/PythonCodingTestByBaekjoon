# t = int(input())
# for _ in range(1, t+1):
#     real_zip = ''
#     tmp = 0
#     ttmp = 0
#     n = int(input())
#     zipp = [list(input().split()) for i in range(n)]
#     alzip = [zipp[i][0]*int(zipp[i][1]) for i in range(n)]
#     for i in range(n):
#         real_zip += alzip[i]
#         tmp += int(zipp[i][1])
#     print(f"#{_}")
#     for i in range(tmp//10):
#         print(f"{real_zip[i*10:i*10+10]}")
#         ttmp = i*10+10
#     print(f"{real_zip[ttmp:]}")
t = int(input())
for _ in range(1, t+1):
    zipp = ''
    tmp = 0
    n = int(input())
    for i in range(n):
        ci, ki = input().split()
        zipp += ci*int(ki)
    print("#{}".format(_))
    for i in range(len(zipp)):
        if (i+1)%10 == 0:
            print(zipp[i])
        else:
            print(zipp[i], end = '')
    if len(zipp) % 10 != 0:
        print()