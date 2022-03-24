arr = []
n = int(input())
max_num = 0
for _ in range(n):
  arr.append(list(map(str,input())))

def width_max():
  global max_num, n
  for i in range(n):
    row_max = 1
    for j in range(n-1):
      if arr[i][j]==arr[i][j+1]:
        row_max +=1
        max_num = max(max_num,row_max)
      else : row_max = 1

def height_max():
  global max_num, n
  for i in range(n):
    column_max = 1
    for j in range(n-1):
      if arr[j][i]==arr[j+1][i]:
        column_max +=1
        max_num = max(max_num,column_max)
      else: column_max = 1

for i in range(n):
  for j in range(n-1):
    if arr[i][j] != arr[i][j+1]:
      arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
      height_max()
      width_max()
      arr[i][j+1],arr[i][j] = arr[i][j],arr[i][j+1] 

    if arr[j][i] != arr[j+1][i]:
      arr[j][i],arr[j+1][i] = arr[j+1][i],arr[j][i]
      height_max()
      width_max()
      arr[j+1][i],arr[j][i] = arr[j][i],arr[j+1][i] 

print(max_num)