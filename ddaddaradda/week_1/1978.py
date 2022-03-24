n=int(input())
arr=list(map(int,input().split()))
count=0

for i in range(n):
    check=True
    if arr[i]==1:
        check=False
    
    for j in range(2,arr[i]):
        if arr[i]%j==0:
            check= False
            break
    if check ==True:
        count+=1

print(count)