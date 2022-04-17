# 모범 답안
import sys
input = sys.stdin.readline
n = int(input())
prices = [0] + list(map(int,input().split()))
max_prices = [0] * (n+1)
max_prices[1] = prices[1]
if n == 1:
  print(max_prices[1])
else:
  for i in range(1,n+1):
    for j in range(1,i+1):
      max_prices[i] = max(max_prices[i],max_prices[i-j]+prices[j])
      
  print(max_prices[n])

# try2 -> 실패 (33%)
import sys 
input = sys.stdin.readline
n = int(input())
prices = [0] + list(map(int,input().split()))
max_prices = [0] * (n+1)

if n == 1:
  max_prices[1] = prices[1]
  print(max_prices[1])
elif n == 2:
  max_prices[1]=prices[1]
  max_prices[2]=max(max_prices[1]*2,prices[2])  
  print(max_prices[2])
elif n == 3:
  max_prices[1]=prices[1]
  max_prices[2]=max(max_prices[1]*2,prices[2])  
  max_prices[3]=max(max_prices[2]+max_prices[1],prices[3])  
  print(max_prices[3])
else:
  max_prices[1]=prices[1]
  max_prices[2]=max(max_prices[1]*2,prices[2])  
  max_prices[3]=max(max_prices[2]+prices[1],prices[3])  
  
  for i in range(4,n+1):
    max_prices[i] = max(max_prices[i-1]+max_prices[1],max_prices[i-2]+max_prices[2])
    max_prices[i] = max(max_prices[i],max_prices[i-3]+max_prices[3])
    max_prices[i] = max(max_prices[i],prices[i])

  print(max_prices[n])

# try 1 -> 실패 (33%)
import sys

input = sys.stdin.readline
n = int(input())
prices = [0] + list(map(int,input().split()))
max_prices = [0] * (n+1)
if n == 1:
  print(prices[1])
elif n == 2:
  max_prices[2]=max(prices[1]*2,prices[2])  
  print(max_prices[2])
elif n == 3:
  max_prices[2]=max(prices[1]*2,prices[2])  
  max_prices[3]=max(max_prices[2]+prices[1],prices[3])  
  print(max_prices[3])
else:
  max_prices[1]=prices[1]
  max_prices[2]=max(prices[1]*2,prices[2])  
  max_prices[3]=max(max_prices[2]+prices[1],prices[3])  
  
  for i in range(4,n+1):
    max_prices[i] = max(max(max_prices[i-1]+max_prices[1],max_prices[i-2]+max_prices[2]),prices[i])

  print(max_prices[n])