n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
ans = 0

def search_max(day,sum):
    global ans
    if day == n :
        ans = max(ans,sum)
        return
    elif day > n :
        return
    search_max(day + arr[day][0],sum + arr[day][1])
    search_max(day+1,sum)
search_max(0,0)
print(ans)