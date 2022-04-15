import itertools
n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

# matrix 1d -> 2d convert(비트마스크를 입력받은 행렬과 같은 모양으로 변형)
def bitmask_to_matrix(l, m):
    return [l[i:i + m] for i in range(0, len(l), m)]

  # itertools의 product를 이용해서 비트마스크 제너레이터 만들기
# e.g) (0,0,0,0), (0,0,0,1) ... (1,1,1,1) 0,1 을 reapeat개수만큼 반복해서 뽑아준다.  
bitmask = itertools.product([0, 1], repeat=n * m)
ans = 0


for x in bitmask:
    # 비트마스크를 N*M 행렬로 변환
    bitmask_matrix = bitmask_to_matrix(x, m)

    # 가로합 저장
    sum_width = 0

    # 가로 계산
    for i in range(n):
        temp_width = 0
        for j in range(m):
            if bitmask_matrix[i][j] == 0:
                temp_width = 10 * temp_width + arr[i][j]
            if bitmask_matrix[i][j] == 1 or j == m - 1:
                sum_width = sum_width + temp_width
                temp_width = 0

    # 세로합 저장
    sum_height = 0

    # 세로 계산
    for j in range(m):
        temp_height = 0
        for i in range(n):
            if bitmask_matrix[i][j] == 1:
                temp_height = 10 * temp_height + arr[i][j]
            if bitmask_matrix[i][j] == 0 or i == n - 1:
                sum_height = sum_height + temp_height
                temp_height = 0

    #가로계산과 세로계산의 합 저장
    sum_all = sum_width + sum_height

    #최대값으로 계속 변경
    ans = max(ans, sum_all)

print(ans)