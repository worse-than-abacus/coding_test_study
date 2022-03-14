# try 1
# 양 끝의 곱 [0] * [-1]
# 성공
import sys
input = sys.stdin.readline
_ = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
print(numbers[0]*numbers[-1])
               


