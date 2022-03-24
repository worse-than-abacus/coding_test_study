n,m=map(int,input().split())
for i in range(n,m+1):
    if i==1: continue
    elif i ==2:
        print(i)
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0 :
                break
        else :
            print(i)