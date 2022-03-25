# try1 -> 실패

import sys
# from collections import deque

input = sys.stdin.readline

n = int(input())
signs = input()
sequences = []

start_i = 0
for i in range(n,0,-1):
  # print(i)
  sequences.append(" "*(n-i)+  signs[start_i:start_i+i])
  start_i += i

table = [[" "]*n for _ in range(n)]
for x in range(n):
  for y in range(n):
    value = sequences[x][y]
    if value != " ":
      table[x][y] = value
      table[y][x] = value
      
    
# print(table)
visited = {key:False for key in range(-10,10+1)}
answer = []
result = " "
def dfs(x,y):
  global answer
  
  if len(answer) == n:
    print(answer)
    return
  if 0<=x<n and 0<=y<n:
    pass
  else:
    return

  if x == y:
    node = table[x][y]
    if node == "+":
      for k in range(1,10+1):
        if not visited[k]:
          visited[k] = True
          answer.append(k)
          dfs(x,y+1)
          answer.pop()
          visited[k] = False
    elif node =="-":
      for k in range(-10,-1+1):
        if not visited[k]:
          visited[k] = True
          answer.append(k)
          dfs(x,y+1)
          answer.pop()
          visited[k] = False
    else:
        k = 0
        if not visited[k]:
          visited[k] = True
          answer.append(k)
          dfs(x,y+1)
          answer.pop()
          visited[k] = False
  else:
    if len(answer) < 2:
      for num in range(answer[0],n):
        answer.append(num)
    if int(answer[-1])+int(answer[-2])  > 0:
      result = "+"
    elif int(answer[-1])+int(answer[-2]) < 0:
      result = "-"
    else:
      result = 0

    if result == table[x][y]:
      dfs(x,y+1)
    else:
      return
    
     

        
          
            
      
for x in range(n):
    for y in range(n):
      dfs(x,y)