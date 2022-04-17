# try 1 -> 성공
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
MAXSUM = -999

def diff_sum(sequence):
  global N
  SUM = 0
  for i in range(N-1):
    SUM += abs(sequence[i]-sequence[i+1])
    
  return SUM

for comb in permutations(A,N):
  MAXSUM = max(MAXSUM, diff_sum(comb))

print(MAXSUM)
  
    


  


