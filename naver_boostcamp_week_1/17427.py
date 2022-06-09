#### 기본적으로 약수를 구할 수 있는 함수를 구현할 수 있나를 물어보는 문제같다.

def getNumDivisor(n):
    divisorlist = []
    for i in range(1, int(n**(1/2))+1) :
        if n % i == 0:
            divisorlist.append(i)
            if (i**2) != n:
                divisorlist.append(n//i)

    sumdivisor = sum(divisorlist)
    return sumdivisor

N = int(input())
ans = 0
for j in range(1, N+1):
    ans = ans + getNumDivisor(j)

print(ans)

#### 1차 fail --> overtime....why??
#### 아 진짜 수학 알고리즘은 수수께끼 같다...
### 최적의 메모리와 시간을 위해 창의력을 모두 사용해야한다....

### 17427 문제의 경우도 약수의 개수의 원리를 이용하여 합을 구하는 방식으로
### 시간과 메모리를 엄청나게 단축시킨다....
## 다시한번 생각하지만 수학과 사람들은 천재다.....

n = int(input())

sumdivisor= 0
for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    sumdivisor += (n//i)*i

print(sumdivisor)

