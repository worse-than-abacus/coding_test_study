import sys
input = sys.stdin.readline

MAX_RANGE = 1_000_000 + 1
table = [True] * MAX_RANGE
table[0], table[1] = False, False

for i in range(MAX_RANGE):
  if table[i]:
    for mi in range(i*2, MAX_RANGE, i):
      table[mi] = False

# 모든 짝수 제거
table[2] = False 

while True:
  n = int(input())
  isWrong = True
  if n == 0 :
    break
  for a in range(3,MAX_RANGE,2):
    if a <= n:
      b = n-a
      # a와 b가 소수이면
      if table[a] & table[b]:
        print(f"{n} = {a} + {b}")
        isWrong = False
        break
  if isWrong:
    print("Goldbach's conjecture is wrong.")