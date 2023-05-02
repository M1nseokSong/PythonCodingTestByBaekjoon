n = int(input())
for i in range(1, n+1):
    clap = 0
    for k in str(i):
        if k in '369':
            clap += 1
    if clap == 0:
        print(i, end=' ')
    else:
        print('-'*clap, end=' ')