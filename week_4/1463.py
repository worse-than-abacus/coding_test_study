

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
while n > 1:
    if n % 3 == 0 :
        n /= 3
        cnt += 1
    elif n % 2 == 0 :
        n /= 2
        cnt += 1
    else :
        n -= 1
        cnt += 1


print(cnt)
