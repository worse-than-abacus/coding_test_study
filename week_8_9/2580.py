import sys

input = sys.stdin.readline

# board = [' '.join(list(map(str, list(input().rstrip())))).split() for _ in range(9)]
board = [list(map(int, input().rstrip().split())) for _ in range(9)]
zeros = []


for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i,j))
print(board)
def checkRow(x, a):
    for i in range(9):
        if a == board[x][i]:
            return False
    return True
def checkCol(y, a):
    for i in range(9):
        if a == board[i][y]:
            return False
    return True
def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return False
    return True
def dfs(idx):
    if idx == len(zeros):
        for i in range(9):
            print(*board[i])
        exit(0)
    for i in range(1, 10):
        x = zeros[idx][0]
        y = zeros[idx][1]
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            board[x][y] = i
            dfs(idx+1)
            board[x][y] = 0
dfs(0)

# from : https://hongcoding.tistory.com/118