# 중간값 찾기
n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[n//2+1]-1)