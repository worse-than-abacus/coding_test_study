from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

n_arr = list(permutations(arr,n))
ans = 0

for i in range(len(n_arr)):
    cur = 0
    for j in range(0,n-1):
        cur += abs(n_arr[i][j] - n_arr[i][j+1])

    if cur > ans :
        ans = cur

print(ans)