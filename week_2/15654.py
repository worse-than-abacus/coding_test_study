# try 1 -> 실패
# 출력 초과
# 중복 출력 존재
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))

selected = []

def search(start):
  for num in numbers:
    if len(selected) == m:
      print(*selected)
      return
    if start == num:
      continue
      
    selected.append(num)
    search(num)
    selected.pop()

search(-1)

# try 2 -> 성공
# 중복 조건 
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
    if num in selected:
      continue
      
    selected.append(num)
    search()
    selected.pop()

search()

