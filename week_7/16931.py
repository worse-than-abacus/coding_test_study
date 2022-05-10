
# 모범답안
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

up = N * M

left = 0
for i in range(N):
    for j in range(M):
        if j == 0:
            left += arr[i][j]
        else:
            if arr[i][j-1] < arr[i][j]:
                left += arr[i][j] - arr[i][j-1]

front = 0
for j in range(M):
    for i in range(N):
        if i == 0:
            front += arr[i][j]
        else:
            if arr[i-1][j] < arr[i][j]:
                front += arr[i][j] - arr[i-1][j]
        
answer = 2 * (up + left + front)
print(answer)


# try1 -> 실패
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
table = []
for _ in range(n):
  row = list(map(int,input().split()))
  table += [row]

square_total = 0

square_total += m*n*2

for row in table:
  square_total += max(row)*2

for col_idx in range(m):
  col = []
  for row_idx in range(n):
    col += [table[row_idx][col_idx]]
  
  square_total += max(col)*2
  square_total += sum(col)-m*min(col)

  col = [value - min(col) for value in col]

  if sum(col) > 1 :
    square_total -= sum(col)
  

print(square_total)