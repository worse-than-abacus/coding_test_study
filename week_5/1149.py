n =  int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = [[0,0,0] for _ in range(n)]
ans[0] = arr[0]
for i in range(1,n):
    ans[i][0] = min(ans[i-1][1],ans[i-1][2])+ arr[i][0]
    ans[i][1] = min(ans[i-1][0],ans[i-1][2])+ arr[i][1]
    ans[i][2] = min(ans[i-1][0],ans[i-1][1])+ arr[i][2]


print(min(ans[n-1]))