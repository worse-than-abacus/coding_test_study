# try 1 -> 성공

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())

s = []

def search():
  for i in range(1,n+1):
    if len(s) == m:
      print(*s)
      return

    s.append(i)
    search()
    s.pop()

search()