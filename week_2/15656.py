# try1 -> 성공
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))

selected = []

def search():
  for num in numbers:
    if len(selected) == m:
      print(*selected)
      return

    selected.append(num)
    search()
    selected.pop()

search()
