import sys, copy
    # , time
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
# start = time.time()
def bfs():
    global answer
    queue = deque()
    temp = copy.deepcopy(board)
    # temp = [[0] * M for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         temp[i][j] = board[i][j]
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if nx < 0 or nx >= N or ny < 0 or ny >=M:
            #     continue
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))
    cnt = 0
    for i in range(N):
        cnt += temp[i].count(0)
    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt+1)
                board[i][j] = 0


# print("temp", temp)
# 벽을 만들어주고 벽이 3개가 되면 bfs를 돌린다
# 0의 갯수 최대치를 출력한다

makeWall(0)
print(answer)
# end_time = time.time()
# print("WorkingTime: {} sec".format(end_time-start))
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간