# 수도 요금 경쟁
T = int(input())
for _ in range(T):
    P, Q, R, S, W = map(int, input().split())
    cost_A = P * W
    if W <= R:
        cost_B = Q
    else:
        cost_B = Q + (W-R)*S
    result = min(cost_A, cost_B)
    print("#%d %d" %(_+1, result))