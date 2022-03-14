# try 1 -> 실패
# 서로소는 특정 구간만 잘라서 계산 할 수 없다.
# 상한은 정할 수 있지만, 하한은 정할 수 없다.
import sys

input = sys.stdin.readline

m, n = map(int,input().split())

# MAX_RANGE = 1_000_000 + 1
MAX_RANGE = n + 1
table = [True] * MAX_RANGE
table[0],table[1] = False, False

for i in range(m,n+1):
  if table[i]:
    for mi in range(i*2, n+1, i):
      table[mi] = False

for i in range(m,n+1):
  if table[i]:
    print(i)


# try 2
import sys
input = sys.stdin.readline
m, n = map(int,input().split())

MAX_RANGE = 1_000_000 + 1
table = [True] * MAX_RANGE
table[0],table[1] = False, False

for i in range(MAX_RANGE):
  if table[i]:
    for mi in range(i*2, MAX_RANGE, i):
      table[mi] = False

for i in range(m,n+1):
  if table[i]:
    print(i)