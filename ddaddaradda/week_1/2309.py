arr = [int(input()) for _ in range(9)]

for i in range(9):
  for j in range(i+1,9):
    if sum(arr) - arr[i] - arr[j] == 100 :
      one,two = arr[i],arr[j]
      break
arr.remove(one),arr.remove(two)
arr.sort()
for i in range(7):
  print(arr[i])