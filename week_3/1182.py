from itertools import combinations
n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
arr2 =[]

for i in range(1,n+1):
  arr2 += list(combinations(arr,i))

for i in range(len(arr2)):
  if sum(arr2[i])==s:
    cnt +=1


print(cnt)