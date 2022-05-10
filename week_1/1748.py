# try 1
import sys
input = sys.stdin.readline
N = int(input())

MAX_RANGE = 10**8
answer = 0
i = 8


while True:

  if N >= 10**i:
    answer += (N-10**i+1) * (i+1)
  print(i, answer)
  i -= 1

  if i < 0:
    break
print(answer)


# try2 
import sys

input = sys.stdin.readline
N = int(input())
n = len(str(N))

ndigit = {i:9*10**(i-1) for i in range(1,8+1)}
answer = 0


for i in range(1, n):
  answer += i*ndigit[i]
answer += n * (N-10**(n-1)+1) 
print(answer)