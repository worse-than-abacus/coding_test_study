# try 2 -> 코드 최적화
# .copy() 안쓰기
import sys
input = sys.stdin.readline
n = int(input())
prices = [0] + list(map(int,input().split()))
min_prices = [0] + [10**7]*n

if n == 1:
  print(min_prices[1])
else:
  for i in range(1, n+1):
    for j in range(1,i+1):
      min_prices[i] = min(min_prices[i],min_prices[i-j]+prices[j])

print(min_prices[n])

# try 1 -> 성공
import sys
input = sys.stdin.readline
n = int(input())
prices = [0] + list(map(int,input().split()))
min_prices = prices.copy()
if n == 1:
  print(min_prices[1])
else:
  for i in range(2, n+1):
    for j in range(1, i):
      min_prices[i] = min(min_prices[i-j]+min_prices[j],min_prices[i])
print(min_prices[n])