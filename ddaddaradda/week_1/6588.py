import sys
M = 1000000
check_arr = [True] * (M+1)
for i in range(2,int(M**0.5)+1):
    for j in range(2*i,M+1,i):
        if check_arr[i] == True:
            if check_arr[j] == True:
                check_arr[j] = False
while True:
    n = int(sys.std.readline.input())
    if n == 0: break
    else:
        for i in range(2,n):
            if check_arr[i] == True and check_arr[n-i] == True:
                print('%d = %d + %d' %(n,i,n-i))
                break
