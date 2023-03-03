# 1대1 가위바위보
a, b = map(int, input().split())
if a==1:
    if b==3:
        print("A")
    else:
        print("B")
elif a==2:
    if a>b:
        print("A")
    else:
        print("B")
else:
    if b==2:
        print("A")
    else:
        print("B")