N,M =map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
max_num=0

def bar1(arr):
  global max_num
  bar1_max = 0
  for i in range(N):
    for j in range(M-3):
      bar1_max=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i][j+3]
      max_num=max(max_num,bar1_max)

def bar2(arr):
  global max_num
  bar2_max = 0
  for i in range(N-3):
    for j in range(M):
      bar2_max=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
      max_num=max(max_num,bar2_max)

def square(arr):
  global max_num
  square_max = 0
  for i in range(N-1):
    for j in range(M-1):
      square_max = arr[i][j]+arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]
      max_num=max(max_num,square_max)

def T1(arr):
  global max_num
  T1_max = 0
  for i in range(N-1):
    for j in range(M-2):
      T1_max = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]
      max_num=max(max_num,T1_max)

def T2(arr):
  global max_num
  T2_max = 0
  for i in range(N-1):
    for j in range(M-2):
      T2_max = arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]+arr[i][j+1]
      max_num=max(max_num,T2_max)

def T3(arr):
  global max_num
  T3_max = 0
  for i in range(N-2):
    for j in range(M-1):
      T3_max = arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+1][j+1]
      max_num=max(max_num,T3_max)

def T4(arr):
  global max_num
  T4_max = 0
  for i in range(N-2):
    for j in range(M-1):
      T4_max = arr[i+1][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
      max_num=max(max_num,T4_max)

def L1(arr): #L모양
  global max_num
  L1_max = 0
  for i in range(N-2):
    for j in range(M-1):
      L1_max = arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]
      max_num=max(max_num,L1_max)

def L2(arr): #L모양 시계 방향 90도 회전
  global max_num
  L2_max = 0
  for i in range(N-1):
    for j in range(M-2):
      L2_max = arr[i+1][j]+arr[i][j]+arr[i][j+1]+arr[i][j+2]
      max_num=max(max_num,L2_max)

def L3(arr): #L모양 180도 회전
  global max_num
  L3_max = 0
  for i in range(N-2):
    for j in range(M-1):
      L3_max = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
      max_num=max(max_num,L3_max)

def L4(arr): #L모양 반시계 방향 90도 회전
  global max_num
  L4_max = 0
  for i in range(N-1):
    for j in range(M-2):
      L4_max = arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]+arr[i][j+2]
      max_num=max(max_num,L4_max)

def dL1(arr): #L모양 좌우 대칭
  global max_num
  dL1_max = 0
  for i in range(N-2):
    for j in range(M-1):
      dL1_max = arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i+2][j]
      max_num=max(max_num,dL1_max)

def dL2(arr): #L모양 좌우 대칭 90도 회전
  global max_num
  dL2_max = 0
  for i in range(N-1):
    for j in range(M-2):
      dL2_max = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+1][j+2]
      max_num=max(max_num,dL2_max)

def dL3(arr): #L모양 좌우 대칭 180도 회전
  global max_num
  dL3_max = 0
  for i in range(N-2):
    for j in range(M-1):
      dL3_max = arr[i][j+1]+arr[i][j]+arr[i+1][j]+arr[i+2][j]
      max_num=max(max_num,dL3_max)

def dL4(arr): #L모양 좌우 대칭 1반시계 90도 회전
  global max_num
  dL4_max =0
  for i in range(N-1):
    for j in range(M-2):
      dL4_max = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+2]
      max_num=max(max_num,dL4_max)

def zig1(arr):
  global max_num
  zig1_max = 0
  for i in range(N-2):
    for j in range(M-1):
      zig1_max = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]
      max_num=max(max_num,zig1_max)

def zig2(arr): # zig1 90도 회전
  global max_num
  zig2_max = 0
  for i in range(N-1):
    for j in range(M-2):
      zig2_max = arr[i+1][j]+arr[i+1][j+1]+arr[i][j+1]+arr[i][j+2]
      max_num=max(max_num,zig2_max)

def dzig1(arr): #zig1 좌우대칭
  global max_num
  dzig1_max = 0
  for i in range(N-2):
    for j in range(M-1):
      dzig1_max = arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j]+arr[i+2][j]
      max_num=max(max_num,dzig1_max)

def dzig2(arr): # dzig1 90도 회전
  global max_num
  dzig2_max = 0
  for i in range(N-1):
    for j in range(M-2):
      dzig2_max = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+1][j+2]
      max_num=max(max_num,dzig2_max)


bar1(arr)
bar2(arr)
square(arr)
T1(arr)
T2(arr)
T3(arr)
T4(arr)
L1(arr)
L2(arr)
L3(arr)
L4(arr)
dL1(arr)
dL2(arr)
dL3(arr)
dL4(arr)
zig1(arr)
zig2(arr)
dzig1(arr)
dzig2(arr)
print(max_num)