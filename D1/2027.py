# 대각선 출력하기
n=5
for _ in range(n):
    print("+"*_,end="")
    print("#",end='')
    print("+"*(n-1-_))