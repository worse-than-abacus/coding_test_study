sudo = []
for i in range(9):
    sudo.append(list(map(int, input().split())))

def check_row(row, column):
    check = [0] * 10
    for i in range(9):
        n = sudo[row][i]
        check[n] = 1
    for j in check:
        if j == 0:
            sudo[row][column] = check.index(j)

def check_column(row, column):
    check = [0] * 10
    for i in range(9):
        n = sudo[i][column]
        check[n] = 1
    for j in check:
        if j == 0:
            sudo[row][column] = check.index(j)

def check_box(row, column):
    check = [0] * 10

# 45 minute -> fail
# my skill so poor



