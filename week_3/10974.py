n =  int(input())
arr = list(i+1 for i in range(n))
ans = []
def dfs():
    if len(ans) ==n:
        print(*ans)
        return
    for x in arr:
        if x not in ans:
            ans.append(x)
            dfs()
            ans.pop()

dfs()