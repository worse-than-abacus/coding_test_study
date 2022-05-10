# 모범 답안

import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def rotate(y, x, height, width):
    global arr
    q = deque()

    for i in range(x, x+width):
        q.append(arr[y][i])
    
    for i in range(y+1, y+height):
        q.append(arr[i][x+width-1])
    
    for i in range(x+width-2, x, -1):
        q.append(arr[y+height-1][i])
    
    for i in range(y+height-1, y, -1):
        q.append(arr[i][x])

    q.rotate(-r)

    for i in range(x, x+width):
        arr[y][i] = q.popleft()
    
    for i in range(y+1, y+height):
        arr[i][x+width-1] = q.popleft()
    
    for i in range(x+width-2, x, -1):
        arr[y+height-1][i] = q.popleft()
    
    for i in range(y+height-1, y, -1):
        arr[i][x] = q.popleft()

height = n
width = m
y, x = 0, 0

while True:
    if height == 0 or width == 0: break

    rotate(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()


# try 1 -> 시간초과!!

import sys
import pprint
input = sys.stdin.readline

N,M,R = map(int,input().split())

raw_table = []
# rotated_table = [[0]*M for _ in range(N)]

for _ in range(N):
  row = list(map(int,input().strip().split()))
  raw_table += [row]


# 가장 외곽에 있는 1줄을 반시계방향으로 회전
def RotatingTable(input_table,order):
  table,rotated_table = [], []
  # deep copy
  for row in input_table:
    rotated_table += [row.copy()]
    table += [row.copy()]
    

  row_len, col_len = len(input_table), len(input_table[0])
      
  for y in range(order,col_len-order):  
    # A 
    x = 0 + order
    if y == 0 + order:
      rotated_table[x+1][y] = table[x][y]
    else: 
      rotated_table[x][y-1] = table[x][y]
  # C
 
    x = row_len-1 - order
    if y == col_len -1 - order:
      rotated_table[x-1][y] = table[x][y]
    else:
      rotated_table[x][y+1] = table[x][y]

  # pprint.pprint(rotated_table)

      
  for x in range(order,row_len-order):
    # B
    y = 0 + order
    if x == row_len -1 - order:
      rotated_table[x][y+1] = table[x][y]
    else:
      rotated_table[x+1][y] = table[x][y]
    # D
    y = col_len-1 - order
    if x ==0 + order:
      rotated_table[x][y-1] = table[x][y]
    else:
      rotated_table[x-1][y] = table[x][y]
      
  # pprint.pprint(rotated_table)

  return rotated_table

rotate_order = range(0,int(len(raw_table)/2))

for _ in range(R):
  for order in rotate_order:
    raw_table = RotatingTable(raw_table,order)



for row in raw_table:
  print(*row)

