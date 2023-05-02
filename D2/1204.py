from collections import defaultdict
t = int(input())
for _ in range(1, t+1):
    n = int(input())
    grade = list(map(int, input().split()))
    math_grade = defaultdict(int)
    for i in grade:
        math_grade[i] += 1
    # math_grade = dict(math_grade)
    result = sorted(math_grade.items(), reverse=True, key=lambda x : (x[1], x[0]))
    print(f"#{_} {result[0][0]}")