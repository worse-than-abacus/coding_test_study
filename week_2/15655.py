N,M = map(int,input().split())
s=[]
num_list=sorted(list(map(int,input().split())))

def dfs(start):
    if len(s)==M:
        print(*s)
        return
    for i in range(start,N):
        s.append(num_list[i])
        dfs(i+1)
        s.pop()
dfs(0)
