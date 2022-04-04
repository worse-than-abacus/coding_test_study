n, m = map(int,input().split())
arr = sorted(list(map(str,input().split())))
s = []
def dfs(start):
    v = 0
    c = 0
    if len(s)==n :
        for x in s :
            if x in 'aeiou' : v+=1 
            else : c+=1
        if v >=1 and c >1:
            print(''.join(s))
            return
        
    for i in range(start,m):
        s.append(arr[i])
        dfs(i+1)
        s.pop()
dfs(0)