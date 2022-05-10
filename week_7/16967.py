# try1 -> 성공
import sys

input = sys.stdin.readline
H, W, X, Y = map(int,input().split())
table = []
A_mat = [[0]*(W) for _ in range(H)]

for _ in range(H+X):
  row = list(map(int,input().split()))
  table += [row]

for x in range(H+X):
  for y in range(W+Y):
    if table[x][y] == 0:
      continue
    elif x < X or y < Y:
      A_mat[x][y] = table[x][y]
    elif H <= x and W <= y:
      A_mat[x-X][y-Y]  = table[x][y]
    elif X <= x < H and Y <= y < W:
      A_mat[x][y] = table[x][y] - A_mat[x-X][y-Y]

for row in A_mat:
  print(*row)