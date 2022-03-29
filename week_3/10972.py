n = int(input())
arr = list(map(int, input().split()))

signal = 0
for i in range(n-1,0,-1):
  if arr[i-1] < arr[i] :
    for j in range(n-1,0,-1):
      if arr[i-1] < arr[j]:
        arr[i-1], arr[j] =  arr[j] , arr[i-1]
        ans = arr[:i] + sorted(arr[i:])
        signal += 1
        break
    if signal == 1:
      print(*ans)
      break
else : print(-1)