# try 1
import sys

input = sys.stdin.readline

k = int(input())
betN= input().split()

visited = [False] * 10

MAX = -1
MIN = 10**10

def search(res,start_idx):
  global MAX, MIN
  if len(res) == k+1:
    # print(res)
    MAX = max(MAX, int(''.join(map(str,res))))
    MIN = min(MIN, int(''.join(map(str,res))))
    return 

  for i in range(10):
    if res[start_idx] == i:
      continue
    
    if '<' == betN[start_idx]:
      if res[start_idx] < i and not visited[i]:
        visited[i] = True
        res.append(i)
        search(res,start_idx+1)
        res.pop()
        visited[i] = False
    elif '>' == betN[start_idx]:
      if res[start_idx] > i and not visited[i]:
        visited[i] = True
        res.append(i)
        search(res,start_idx+1)
        res.pop()
        visited[i] = False




for start_num in range(10):
  search([start_num],0)

print(MAX)
print(MIN)

# try 2 -> 성공, 초기 방문 처리 추가
import sys

input = sys.stdin.readline

k = int(input())
betN= input().split()

visited = [False] * 10

MAX = -1
MIN = 10**10

def search(res,start_idx):
  global MAX, MIN, visited
  if len(res) == k+1:
    # print(res)
    MAX = max(MAX, int(''.join(map(str,res))))
    MIN = min(MIN, int(''.join(map(str,res))))
    return 

  for i in range(10):
    if res[start_idx] == i:
      continue
    
    if '<' == betN[start_idx]:
      if res[start_idx] < i and not visited[i]:
        visited[i] = True
        res.append(i)
        search(res,start_idx+1)
        res.pop()
        visited[i] = False
    elif '>' == betN[start_idx]:
      if res[start_idx] > i and not visited[i]:
        visited[i] = True
        res.append(i)
        search(res,start_idx+1)
        res.pop()
        visited[i] = False




for start_num in range(10):
  visited[start_num] = True
  search([start_num],0)
  visited[start_num] = False

print("0"*(k+1-len(str(MAX))),end="")
print(MAX)
print("0"*(k+1-len(str(MIN))),end="")
print(MIN)


        
        
          