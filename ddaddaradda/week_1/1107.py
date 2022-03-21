target = int(input())
n = int(input())
b_num = list(map(int,input().split()))

min_num = abs(100-target)
for i in range(1000001):
  num = str(i)
  for j in range(len(num)):
    if int(num[j]) in b_num:
      break
    elif j == (len(num)-1):
      min_num=min(min_num,abs(int(num)-target)+len(num))
print(min_num)
