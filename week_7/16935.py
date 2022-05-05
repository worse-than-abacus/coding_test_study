import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# print(board)


# 1 연산 상하반전
def function1():
    # print("팡션1")
    board.reverse()


# 2 연산 좌우반전
def function2():
    # print("팡션2")
    for row in board:
        row.reverse()


# 3 연산 오른쪽으로 90도 회전
def function3():
    # print("팡션3")
    global board
    N = len(board)
    M = len(board[0])
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = board[N - j - 1][i]

            # temp[j][M - i - 1] = board[i][j]
    board = temp


# # 4 연산 왼쪽으로 90도 회전
def function4():
    # print("팡션4")
    global board
    N = len(board)
    M = len(board[0])
    temp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp[i][j] = board[j][M - i - 1]
            # temp[N - j - 1][i] = board[i][j]
    board = temp


# # 5 연산 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동
def function5():
    # print("팡션5")
    global board
    N = len(board)
    M = len(board[0])
    temp = [[0] * M for _ in range(N)]
    h_ln = int(N / 2)
    v_ln = int(M / 2)
    # 1 -> 2
    for i in range(h_ln):
        # 1 -> 2
        temp[i][v_ln:] = board[i][:v_ln]
        # 2 -> 3
        temp[h_ln + i][v_ln:] = board[i][v_ln:]
        # 3 -> 4
        temp[h_ln + i][:v_ln] = board[h_ln + i][v_ln:]
        # 4 -> 1
        temp[i][:v_ln] = board[h_ln + i][:v_ln]
    board = temp[:]


# # 6 연산 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동
def function6():
    # print("팡션6")
    global board
    N = len(board)
    M = len(board[0])
    temp = [[0] * M for _ in range(N)]
    h_ln = int(N / 2)
    v_ln = int(M / 2)
    for i in range(h_ln):
        # 1 -> 4
        temp[h_ln + i][:v_ln] = board[i][:v_ln]
        # 2 -> 1
        temp[i][:v_ln] = board[i][v_ln:]
        # 3 -> 2
        temp[i][v_ln:] = board[h_ln + i][v_ln:]
        # 4 -> 3
        temp[h_ln + i][v_ln:] = board[h_ln + i][:v_ln]
    board = temp[:]


operation = list(map(int, input().split()))
# print("오퍼레이션", operation)

operation_dict = {1: function1, 2: function2, 3: function3, 4: function4, 5: function5, 6: function6}

for i in operation:
    # print("i : ", i)
    func = operation_dict[i]
    func()
    answer = list(board)
for row in answer:
    print(*row, sep=' ')
