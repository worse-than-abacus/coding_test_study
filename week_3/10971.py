n = int(input())
table = [list(map(int,input().split())) for _ in range(n) ]

visited = [False] * n
answer = 0

MINSUM = 10**7+1


def search(start,first):
  global answer, MINSUM, n
  
  if sum(visited) == n and first == start:
    MINSUM= min(MINSUM, answer)
    return
  

  for end in range(n):
    if not visited[end] and table[start][end] != 0:
      visited[end] = True
      answer += table[start][end]
      search(end,first)
      answer -= table[start][end]
      visited[end] = False
    
search(0,0)

print(MINSUM)