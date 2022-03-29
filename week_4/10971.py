# try1->실패
import sys

input = sys.stdin.readline

N = int(input())
table = []
for _ in range(N):
  row = list(map(int,input().split()))
  table += [row]

visited = [False] * N 
answer = 0
MINSUM = 10*6

def search():
  global answer, N, MINSUM
  
  if sum(visited) == N:
    MINSUM = min(answer, MINSUM)
    return 

  for i in range(N): # 출발
    for j in range(N): # 도착
      if not visited[i] and table[i][j] != 0 and i != j:
        visited[j] = False
        answer += table[i][j]
        search()
        answer -= table[i][j]
        visited[j] = False



search()   
print(MINSUM)


# try 2-> 실패
import sys


input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N):
  row = list(map(int,input().split()))
  table += [row]

visited = [False] * N 
answer = 0

MINSUM = 10**6


def search(start,first):
  global answer, MINSUM, N
  
  if sum(visited) == N and first == start:
    MINSUM= min(MINSUM, answer)
    return
  

  for end in range(N):
    if not visited[end] and table[start][end] != 0 and start != end:
      visited[end] = True
      answer += table[start][end]
      search(end,first)
      answer -= table[start][end]
      visited[end] = False
    
# for start in range(N):
#     search(start,start)
search(0,0)

print(MINSUM)

# try 3 -> 성공
import sys


input = sys.stdin.readline
N = int(input())
table = []
for _ in range(N):
  row = list(map(int,input().split()))
  table += [row]

visited = [False] * N 
answer = 0

MINSUM = 10**7+1


def search(start,first):
  global answer, MINSUM, N
  
  if sum(visited) == N and first == start:
    MINSUM= min(MINSUM, answer)
    return
  

  for end in range(N):
    if not visited[end] and table[start][end] != 0:
      visited[end] = True
      answer += table[start][end]
      search(end,first)
      answer -= table[start][end]
      visited[end] = False
    
search(0,0)

print(MINSUM)