# 비밀번호
# D3
for tc in range(1, 11):
    n, password = input().split()
    password = list(password)
    while(True):
        tmp = 0
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                tmp = 1
                password.pop(i-1)
                password.pop(i-1)
                break
        if tmp == 0:
            break


    print("#{} {}" .format(tc, ''.join(password)))
