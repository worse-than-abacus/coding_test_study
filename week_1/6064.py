# try1 -> 시간초과

import sys
input = sys.stdin.readline
T = int(input())

MAX_RANGE = 40_000

for _ in range(T):
  year = 0
  isSearching = True
  M,N,x,y = list(map(int,input().split())) 
  while isSearching:
    if year%M == x-1:
      if year%N == y-1:
        print(year+1)
        isSearching = False

    if year  >= M*MAX_RANGE or year >= N * MAX_RANGE:
      print(-1)
      isSearching = False
    year += 1

# try 2
# 시간 초과

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  year = 0
  isSearching = True
  M,N,x,y = list(map(int,input().split())) 
  i = 0
  while True:
    
    
    year = i*M + x
    # 나머지를 [1, N]로 만들기
    if (year-1) % N + 1 == y:
      print(year)
      break

    if year > M*N + 1:
      print(-1)
      break
    i += 1

# try 3 -> 성공 (w. pypy3)
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  year = 0
  isSearching = True
  M,N,x,y = list(map(int,input().split())) 
  i = 0
  while True:

    year = i*M + x
    # 나머지를 [1, N]로 만들기
    if (year-1) % N + 1 == y:
      print(year)
      break

    if year > M*N + 1:
      print(-1)
      break
    i += 1

# try 4 -> 성공 (모범답안, python 3)
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m,n,x,y = map(int,input().split())
    ans = -1
    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    print(ans)  