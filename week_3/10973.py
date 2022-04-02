# try 1 -> 시간 초과
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
target_seq = list(map(int,input().split()))
seq = list(range(1,N+1))


def find_target():
  pre_seq = None
  for comb in permutations(seq,N):
    for i in range(len(comb)):
      if comb[i] != target_seq[i]:
        break
    else:
      if pre_seq is None:
        print(-1)
      else:
        print(" ".join(map(str,pre_seq)))
        return
    
    pre_seq = comb

find_target()