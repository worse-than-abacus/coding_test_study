N, M = map(int,input().split())
s=[]
num_list=sorted(list(map(int,input().split())))

def dfs():
    if len(s)==M:
        print(*s)
        return
    for i in range(N):
        s.append(num_list[i])
        dfs()
        s.pop()

dfs()