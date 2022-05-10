# Try1 10:15

n, k = map(int, input().split())
arr = list(map(int, input().split()))
point = [0] * n

def solve(num):
    total = 0
    for i in range(num, n):
        total += arr[i]
        if total >= k:
            break
    return total

for j in range(n):
    point[j] = solve(j) 

print(point.count(k))        

# fail: overtime
# 17%에 엄청난 시간초과를 넣어놓은 듯....
# pypy3 에서는 success