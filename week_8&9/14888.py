# 10:30 시작 (중간 쉬는시간 15분)
from decimal import MIN_EMIN
from multiprocessing.connection import answer_challenge
from tkinter.tix import MAX


n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
oper = []
MAX = -10**10
MIN = 10**10
cnt = 0
check = [0] * n

def switch_oper():
    global cal, oper
    if cal[0] > 0:
        a = cal[0]
        oper += ['+'] * a

    if cal[1] > 0:
        a = cal[1]
        oper += ['-'] * a

    if cal[2] > 0:
        a = cal[2]
        oper += ['*'] * a

    if cal[3] > 0:
        a = cal[3]
        oper += ['/'] * a

def solve(): 
    global oper, MIN, MAX, num, cnt

    if cnt == n:
        if answer > MAX:
            MAX = answer
        if answer < MIN:
            MIN = answer
        return
    
    for i in range(n-1): # 부등호 고정
        for j in range(n) :

# 11:20 -> fail
# 아 너무 어렵게 생각하고 만든 것 같다...
# 원래 하고 싶었던 아이디어는 부등호, 숫자 중 하나를 고정시키고 나머지를 모두 둘러보는 dfs를 구현하고 싶었는데
# 너무 카운트, 등호, 등등 너무 복잡하게 생각
# 있는 것을 최대한 활용하고 
# 그게 안될 때 새로운 리스트나 변수 등을 만들 생각을 해야한다... 명심!!!!

# 방법은 2자기 dfs, permutation

# 1. dfs
import sys
input = sys.stdin.readline
def dfs(cnt, result, p, m, mul, div):
    global max_result
    global min_result
    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    if p:
        dfs(cnt + 1, result + s[cnt], p - 1, m, mul, div)
    if m:
        dfs(cnt + 1, result - s[cnt], p, m - 1, mul, div)
    if mul:
        dfs(cnt + 1, result * s[cnt], p, m, mul - 1, div)
    if div:
        dfs(cnt + 1, -(-result // s[cnt]) if result < 0 else result // s[cnt], p, m, mul, div - 1)
n = int(input())
s = list(map(int, input().split()))
op = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
dfs(1, s[0], op[0], op[1], op[2], op[3])
print(max_result)
print(min_result)

# 2. permutation -> 시간초과 // pypy -> 통과
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -1e9
minimum = 1e9


def solve():
    global maximum, minimum
    for case in permutations(op, N - 1):
        total = num[0]
        for r in range(1, N):
            if case[r - 1] == '+':
                total += num[r]
            elif case[r - 1] == '-':
                total -= num[r]
            elif case[r - 1] == '*':
                total *= num[r]
            elif case[r - 1] == '/':
                total = int(total / num[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total


solve()
print(maximum)
print(minimum)

    