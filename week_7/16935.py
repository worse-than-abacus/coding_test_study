# try 1 -> 성공
import sys
import itertools

input = sys.stdin.readline
n,m,r = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]
fun_numbers = list(map(int,input().split()))

rotated_table = [[0]*n for _ in range(m)]

for fun_num in fun_numbers:
  n, m = len(table), len(table[0])
  
  if fun_num == 1:
    table.reverse()
  elif fun_num == 2:
    for row_idx in range(n):
      table[row_idx].reverse()
  elif fun_num == 3:
    rotated_table = []
    for col_idx in range(m): # 원본 행렬의 열
      col = []
      for row_idx in range(n): # 원본 행렬의 행
        col += [table[row_idx][col_idx]]
      
      col.reverse()
      rotated_table += [col]
    table = rotated_table

  elif fun_num == 4:
    for row_idx in range(n):
      table[row_idx].reverse()
    rotated_table = []

    
    for col_idx in range(m): # 원본 행렬의 열
      col = []
      for row_idx in range(n): # 원본 행렬의 행
        col += [table[row_idx][col_idx]]
   
      rotated_table += [col]
    table = rotated_table

  elif fun_num == 5:
    # group_idx
    new_table = [[0]*m for _ in range(n)]
    
    group1 = list(itertools.product(list(range(0,int(n//2))),list(range(0,int(m//2)))))
    group2 = list(itertools.product(list(range(0,int(n//2))),list(range(int(m//2),m))))
    group3 = list(itertools.product(list(range(int(n//2),n)),list(range(int(m//2),m))))
    group4 = list(itertools.product(list(range(int(n//2),n)),list(range(0,int(m//2)))))
    
    
    # group 1 -> group 2
    for (x,y),(new_x,new_y) in zip(group1,group2):
        new_table[new_x][new_y] = table[x][y]
    
    # group 2 -> group 3
    for (x,y),(new_x,new_y) in zip(group2,group3):
        new_table[new_x][new_y] = table[x][y]
    
    # group 3 -> group 4
    for (x,y),(new_x,new_y) in zip(group3,group4):
        new_table[new_x][new_y] = table[x][y]
    
    # group 4 -> group 1
    for (x,y),(new_x,new_y) in zip(group4,group1):
        new_table[new_x][new_y] = table[x][y]

    table = new_table
    
  elif fun_num == 6:
    # group_idx
    new_table = [[0]*m for _ in range(n)]
    
    group1 = list(itertools.product(list(range(0,int(n//2))),list(range(0,int(m//2)))))
    group2 = list(itertools.product(list(range(0,int(n//2))),list(range(int(m//2),m))))
    group3 = list(itertools.product(list(range(int(n//2),n)),list(range(int(m//2),m))))
    group4 = list(itertools.product(list(range(int(n//2),n)),list(range(0,int(m//2)))))
    
    
    # group 1 -> group 4
    for (x,y),(new_x,new_y) in zip(group1,group4):
        new_table[new_x][new_y] = table[x][y]
    
    # group 4 -> group 3
    for (x,y),(new_x,new_y) in zip(group4,group3):
        new_table[new_x][new_y] = table[x][y]
    
    # group 3 -> group 2
    for (x,y),(new_x,new_y) in zip(group3,group2):
        new_table[new_x][new_y] = table[x][y]
    
    # group 2 -> group 1
    for (x,y),(new_x,new_y) in zip(group2,group1):
        new_table[new_x][new_y] = table[x][y]

    table = new_table

      
for row_idx in range(len(table)):
  print(*table[row_idx])