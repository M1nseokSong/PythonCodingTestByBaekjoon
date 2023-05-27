# 민석이의 과제 체크
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    hw = list(map(int, input().split()))
    student = []
    for i in range(1, n+1):
        if i not in hw:
            student.append(i)
    print(f"#{tc}", end=' ')
    print(*student)
