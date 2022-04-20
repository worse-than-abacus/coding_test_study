# try1 시간초과
for _ in range(int(input())):
    M, N, x, y = map(int,input().split())
    n_x, n_y, cnt = 1, 1, 2
    for i in range(N*M):
        if n_x == x and n_y == y :
            break
        else :
            n_x += 1
            if n_x>M:
                n_x = n_x-M
            n_y += 1
            if n_y>N:
                n_y = n_y-N
            cnt += 1
    if cnt > N*M : 
        print(-1)
    else:
        print(cnt-1)


#
import sys
for _ in range(int(sys.stdin.readline())):
    M, N, x, y = map(int,sys.stdin.readline().split())
    ans = -1
    while x <= M * N:
        if (x - y) % N == 0:
            ans = x
            break
        x += M
    print(ans)