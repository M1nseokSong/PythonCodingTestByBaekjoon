# 암호문3
for _ in range(10):
    n = int(input())
    passwd = list(map(int, input().split()))
    m = int(input())
    command = list(input().split())
    change = []
    for i in range(len(command)):
        if command[i] == 'I':
            for j in range(int(command[i+2])):
                passwd.insert(int(command[i+1])+j, command[i+3+j])
        elif command[i] == 'D':
            for j in range(int(command[i+2])):
                passwd.pop(int(command[i+1])+j)
        elif command[i] == 'A':
            for j in range(int(command[i+1])):
                passwd.append(command[i+2+j])
    print(f"#{_+1}", end=' ')
    print(*[passwd[k] for k in range(5)])
