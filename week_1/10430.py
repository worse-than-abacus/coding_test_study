
# try 1 , 성공



import sys
input = sys.stdin.readline
A, B, C = list(map(int,input().split()))

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print((A%C)*(B%C)%C)