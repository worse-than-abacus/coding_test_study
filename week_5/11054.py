# 모범답안
import sys
input =sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n
dp = [0] * n

reverse_case = case[::-1]

for i in range(n):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0] * n
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] -1

print(max(result))