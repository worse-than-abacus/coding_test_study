# try1 -> 실패
# 모범답안
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
T = int(input())

def sol(n):
  if n == 1:
    return 1

  elif n == 2:
    return 2
  elif n == 3:
    return 4

  else:
    return sol(n-1)+sol(n-2)+sol(n-3)

for _ in range(T):
  n = int(input())
  print(sol(n))