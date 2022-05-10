# try 1 -> 성공
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))

selected = []

def search(start):
  for idx in range(start,len(numbers)):
    if len(selected) == m:
      print(*selected)
      return

    selected.append(numbers[idx])
    search(idx)
    selected.pop()

search(0)