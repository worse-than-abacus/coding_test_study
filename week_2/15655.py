# try 1 -> 성공
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
selected = []


def search(start):
  if len(selected) == m:
    print(*selected)
    return

  for idx in range(start,len(numbers)):
    selected.append(numbers[idx])
    search(idx+1)
    selected.pop()

search(0)