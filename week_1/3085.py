import sys

input = sys.stdin.readline


n = int(input())
table = []
for _ in range(n):
  row = list(input())
  table += [row]
  
  # row = input()
  # table += [value for value in row]

  
def max_check(table):
  MAX = 0
  for i in range(n):
    rowcnt, colcnt = 1, 1
    for next_idx in range(1,n):
      # 행 검사
      if table[i][next_idx-1] == table[i][next_idx]:
        rowcnt += 1
      else:
        rowcnt = 1

      # 열 검사
      if table[next_idx-1][i] == table[next_idx][i]:
        colcnt += 1
      else:
        colcnt = 1

      if MAX < rowcnt:
        # print(MAX,rowcnt,i,next_idx)
        MAX = rowcnt
        
  
      if MAX < colcnt:
        # print(MAX,colcnt,i,next_idx)
        MAX = colcnt
        
  return MAX

MAX = max_check(table)
print(MAX)


for x in range(n):
  for y in range(n):  
  # 다음 값하고 바꾸고
    
    if y + 1 < n:
      table[x][y], table[x][y+1] = table[x][y+1], table[x][y]
      now = max_check(table)
    # 원래대로 복구
      table[x][y], table[x][y+1] = table[x][y+1], table[x][y]
      if MAX < now:
        MAX = now
        print("y",MAX)
  # 다음 값하고 바꾸고
    if x + 1 < n:
      table[x][y], table[x+1][y] = table[x][y], table[x+1][y]
      now = max_check(table)
    # 원래대로 복구
      table[x][y], table[x+1][y] = table[x][y], table[x+1][y]
      if MAX < now:
        MAX = now
        print("x",MAX)
      

print(MAX)
    

# try2 -> 실패
# newtable = table.copy()
import sys
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
  row = list(input())
  table += [row]

MAX = 0
def max_check(table):
  global MAX
  for i in range(n):
    rowcnt, colcnt = 1, 1
    for next_idx in range(1,n):
      # 행 검사
      if table[i][next_idx-1] == table[i][next_idx]:
        rowcnt += 1
        MAX = max(rowcnt,MAX)
      else:
        rowcnt = 1

      # 열 검사
      if table[next_idx-1][i] == table[next_idx][i]:
        colcnt += 1
        MAX = max(colcnt,MAX)
      else:
        colcnt = 1

  return MAX

MAX = max_check(table)
dx = [1,0]# 아래, 오른쪽
dy = [0,1]

for x in range(n):
  for y in range(n):
    for i in range(2):
      next_x, next_y = x+dx[i], y+dy[i]
      if next_x < n and next_y < n:
        newtable = table.copy()
        newtable[x][y], newtable[next_x][next_y] = newtable[next_x][next_y], newtable[x][y]
        max_check(newtable)
        
    
print(MAX)
    

# try3 -> 성공
# 모범 답안(과거 코드)
n = int(input())
candies=[]
ans = 1
 
for i in range(n):
    temp =[]
    temp_str = input()
    for j in range(n):
        temp.append(temp_str[j])
    candies.append(temp)
    

    
# 몇개 먹을 수 있는지 찾는 함수
def search():
    global ans
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[i][j]== candies[i][j+1]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        #ans = max(cnt,ans)
        
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        #ans = max(cnt,ans)
        


# [모든 인접한 두 자리 뒤집어보고 찾기]    
# 가로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
        search()
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]

# 세로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]
        search()
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]

        
print(ans)


# try 4
import sys
input = sys.stdin.readline
# copy() 대신 바꾸고, 검사하고, 복구하는 방법 사용
n = int(input())
table = []
for _ in range(n):
  row = list(input())
  table += [row]

MAX = 0
def max_check(table):
  global MAX
  for i in range(n):
    rowcnt, colcnt = 1, 1
    for next_idx in range(1,n):
      # 행 검사
      if table[i][next_idx-1] == table[i][next_idx]:
        rowcnt += 1
        MAX = max(rowcnt,MAX)
      else:
        rowcnt = 1

      # 열 검사
      if table[next_idx-1][i] == table[next_idx][i]:
        colcnt += 1
        MAX = max(colcnt,MAX)
      else:
        colcnt = 1
dx = [1,0]# 아래, 오른쪽
dy = [0,1]
for x in range(n):
  for y in range(n):
    for i in range(2):
      next_x, next_y = x+dx[i], y+dy[i]
      if next_x < n and next_y < n:
        table[x][y], table[next_x][next_y] = table[next_x][next_y], table[x][y]
        max_check(table)
        table[x][y], table[next_x][next_y] = table[next_x][next_y], table[x][y]
        
    
print(MAX)


# try 5-> 실패, 시간초과 
# copy.deepcopy() 말고 깊은 복사 방법이 있을까
import copy
import sys
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
  row = list(input())
  table += [row]

MAX = 0
def max_check(table):
  global MAX
  for i in range(n):
    rowcnt, colcnt = 1, 1
    for next_idx in range(1,n):
      # 행 검사
      if table[i][next_idx-1] == table[i][next_idx]:
        rowcnt += 1
        MAX = max(rowcnt,MAX)
      else:
        rowcnt = 1

      # 열 검사
      if table[next_idx-1][i] == table[next_idx][i]:
        colcnt += 1
        MAX = max(colcnt,MAX)
      else:
        colcnt = 1

  return MAX

MAX = max_check(table)
dx = [1,0]# 아래, 오른쪽
dy = [0,1]

for x in range(n):
  for y in range(n):
    for i in range(2):
      next_x, next_y = x+dx[i], y+dy[i]
      if next_x < n and next_y < n:
        newtable = copy.deepcopy(table)
        newtable[x][y], newtable[next_x][next_y] = newtable[next_x][next_y], newtable[x][y]
        max_check(newtable)
        
    
print(MAX)


# try 6 -> 실패
# table[:][:] = 얕은 복사 
# try 2와 동일 (5%에서 실패)
import sys
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
  row = list(input())
  table += [row]

MAX = 0
def max_check(table):
  global MAX
  for i in range(n):
    rowcnt, colcnt = 1, 1
    for next_idx in range(1,n):
      # 행 검사
      if table[i][next_idx-1] == table[i][next_idx]:
        rowcnt += 1
        MAX = max(rowcnt,MAX)
      else:
        rowcnt = 1

      # 열 검사
      if table[next_idx-1][i] == table[next_idx][i]:
        colcnt += 1
        MAX = max(colcnt,MAX)
      else:
        colcnt = 1

  return MAX

MAX = max_check(table)
dx = [1,0]# 아래, 오른쪽
dy = [0,1]

for x in range(n):
  for y in range(n):
    for i in range(2):
      next_x, next_y = x+dx[i], y+dy[i]
      if next_x < n and next_y < n:
        newtable = table[:][:]
        newtable[x][y], newtable[next_x][next_y] = newtable[next_x][next_y], newtable[x][y]
        max_check(newtable)
        
    
print(MAX)