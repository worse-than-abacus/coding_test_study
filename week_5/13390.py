# try1 메모리초과
n = int(input())
arr = list(map(int,input().split()))
n_arr = [arr[:] for _ in range(n+1)]

for i in range(n):
    n_arr[i][i] = 0

T_dp =[0]*(n+1)
for i in range(n+1):
    dp = [0]*(n)
    dp[0] = n_arr[i][0]
    for j in range(1,n):
        dp[j] = max(dp[j-1]+n_arr[i][j],n_arr[i][j])
    T_dp[i] = max(dp)
print(max(T_dp))


# try2 시간초과
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) + [0]

T_dp =[0]*(n+1)
for i in range(n+1):
    n_arr = arr[:]
    n_arr[i] = 0
    dp = [0]*(n)
    dp[0] = n_arr[0]
    for j in range(1,n):
        dp[j] = max(dp[j-1]+n_arr[j],n_arr[j])
    T_dp[i] = max(dp)
    n_arr = arr[:]
print(max(T_dp))

# try3
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[x for x in arr] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + arr[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])

print(max(max(dp[0]), max(dp[1])))
