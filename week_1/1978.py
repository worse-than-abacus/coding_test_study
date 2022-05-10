# try 1
import sys
input = sys.stdin.readline

_ = int(input())
numbers = list(map(int,input().split()))

MAX_RANGE = 1000+1
table = [True] * MAX_RANGE
table[0],table[1] = False,False


for i in range(2,MAX_RANGE):
  if table[i]: # 한번도 방문 안했으면
    # table[i] = True
    # print(i,end=" ")
    for mi in range(i*2, MAX_RANGE, i):
      table[mi] = False # i의 배수 전부 False

answer = 0
for num in numbers:
  if table[num]:
    answer += 1

print(answer)