n, s = map(int, input().split())
arr = list(map(int, input().split()))
point = [0] * n

def solve(num):
    total = 0
    cnt = 0
    for i in range(num, n):
        total += arr[i]
        cnt += 1
        if total >= s:
            break
    return cnt

for j in range(n):
    point[j] = solve(j)

if sum(arr) < s:
    print(0)
else :
    print(min(point))

# fail -> 이렇게 하면 뒤에서 조건이 맞지 않는 녀석도 카운트가 저장이 된다..
# Try2

n, s = map(int, input().split())
arr = list(map(int, input().split()))
point = [0] * n

def solve(num):
    total = 0
    cnt = 0
    for i in range(num, n):
        total += arr[i]
        cnt += 1
        if total >= s:
            return cnt
            break
    if total < s:
        return 10001
            

for j in range(n):
    point[j] = solve(j)

MIN = min(point)

if MIN > n :
    print(0)
else :
    print(MIN)

# fail -> overtime
# Try3 pypy3 & sys
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
point = [0] * n

def solve(num):
    total = 0
    cnt = 0
    for i in range(num, n):
        total += arr[i]
        cnt += 1
        if total >= s:
            return cnt
            break
    if total < s:
        return 10001
            

for j in range(n):
    point[j] = solve(j)

MIN = min(point)

if MIN > n :
    print(0)
else :
    print(MIN)

# fail....
# two point 개념에서 다시 풀어보자
# https://dev-dain.tistory.com/152 answer sheet

