
# 모범답안 1
from collections import deque

s = int(input())
queue = deque()
queue.append((1, 0))  # [현재 이모티콘 개수, 클립보드 이모티콘 개수]
visited = dict()
visited[(1, 0)] = 0 # 최소 시간!

while queue:
    screen, board = queue.popleft()
    if screen == s:
        print(visited[(screen, board)])
        break
        
    # 1번 연산 : 화면에 있는 모든 이모티콘을 복사
    ## (screen,screen) : 복사를 안했으면 -> 복사
    if (screen, screen) not in visited.keys():
        visited[(screen, screen)] = visited[(screen, board)] + 1
        queue.append((screen, screen))

    # 2번 : 화면에 있는 모든 이모티콘 중 1개 삭제
    if (screen-1, board) not in visited.keys():
        visited[(screen-1, board)] = visited[(screen, board)] + 1
        queue.append((screen-1, board))

    # 3번 연산 : 클립보드에 있는 이모티콘을 붙여넣기
    if (screen+board, board) not in visited.keys():
        visited[(screen+board, board)] = visited[(screen, board)] + 1
        queue.append((screen+board, board))


# 모범답안 2
import sys
from collections import deque
S=int(input())
visited=[[-1]*3001 for _ in range(3001)]
 
def bfs(left,right):
    q=deque()
    q.append([left,right])
    visited[left][right]=0
    while q:
        emoti,clip=q.popleft()
        if emoti==S:
            break
        if clip:
            if visited[emoti+clip][clip]==-1 and emoti+clip<=S:
                visited[emoti+clip][clip]=visited[emoti][clip]+1
                q.append([emoti+clip,clip])
 
            if visited[emoti][emoti]==-1:
                q.append([emoti,emoti])
                visited[emoti][emoti]=visited[emoti][clip]+1
 
            if visited[emoti-1][clip]==-1 and emoti-1>0:
                visited[emoti-1][clip]=visited[emoti][clip]+1
                q.append([emoti-1,clip])
        else:
            q.append([emoti,emoti])
            visited[emoti][emoti]=visited[emoti][clip]+1
        
bfs(1,0)
ans=10e9
for i in range(S+1):
    if visited[S][i]!=-1:
        ans=min(ans,visited[S][i])
print(ans)
