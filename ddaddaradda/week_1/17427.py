# 시간초과
n = int(input())
ans=0
for i in range(1,n+1):
    for j in range(1,int(i**0.5)+1):
        if i%j==0: 
            m = i/j
            if m==j:
                 ans+=j
            else:
                ans+=(j+m)
print(int(ans))

# f(x)구하지 말고
n = int(input())
sum=0
for i in range(1,n+1):
    sum += (n//i)*i
print(sum)