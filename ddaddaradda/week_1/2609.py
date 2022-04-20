A,B = map(int,input().split())
for i in range(A,0,-1):
    if A%i==0 and B%i==0:
         gcd = i
         break
print(gcd)
print(int(A*B/gcd))