# try 2 -> 코드 최적화
# exit()는 프로그램 전체 종료, 사용하기 곤란한 경우 많음
# if로 대체
import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3,n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(dp[n] % 10007)


# try 1 -> 성공
import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3,1001):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n] % 10007)