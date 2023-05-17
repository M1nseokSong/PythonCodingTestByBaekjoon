# D3
# 보충학습과 평균
tc = int(input())
for t in range(1, tc+1):
    score = list(map(int, input().split()))
    new_score = [i if i >= 40 else 40 for i in score]
    print(f"#{t} {sum(new_score)//5}")
