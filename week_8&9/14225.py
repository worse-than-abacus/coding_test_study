#
n = int(input())
s = list(map(int, input().split()))
check = [0] * (100000 * 3 -3)
check[0] = 1

from itertools import combinations

for j in range(1, n+1):
    for i in combinations(s, j):
        total = sum(i)
        if check[total] == 0:
            check[total] = 1

print(check.index(min(check)))

# fail -> index error
# try2

n = int(input())
s = list(map(int, input().split()))
check = [0] * 2000001 # 아... 범위 설정 오류ㅠ
check[0] = 1

from itertools import combinations

for j in range(1, n+1):
    for i in combinations(s, j):
        total = sum(i)
        if check[total] == 0:
            check[total] = 1

print(check.index(min(check)))

# success!!