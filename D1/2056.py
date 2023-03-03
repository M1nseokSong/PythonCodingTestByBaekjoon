# 연월일 달력
t = int(input())
for _ in range(t):
    n = input()
    year = n[0:4]
    month = n[4:6]
    day = n[6:8]
    days= {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        print("#%d %s/%s/%s" %(_+1, year,month,day))
    else:
        print("#%d -1" %(_+1))