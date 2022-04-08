n = int(input())
rgb = []
min_cost =[0]*3
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, len(rgb)):
    min_cost[0] += (rgb[i][0] + min(rgb[i-1][1], rgb[i-1][2]))
    min_cost[1] += (rgb[i][1] + min(rgb[i-1][0], rgb[i-1][2]))
    min_cost[2] += (rgb[i][2] + min(rgb[i-1][0], rgb[i-1][1]))

print(min(min_cost))

# try1 -> fail (중복으로 값이 더해진다...)

n = int(input())
rgb = []
min_cost =[0]*3
for _ in range(n):
    rgb.append(list(map(int, input().split())))
min_cost[0], min_cost[1], min_cost[2] = rgb[0][0], rgb[0][1], rgb[0][2]
for i in range(1, len(rgb)):
    min_cost[0] += min(rgb[i-1][1], rgb[i-1][2])
    min_cost[1] += min(rgb[i-1][0], rgb[i-1][2])
    min_cost[2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(min_cost))

# try2 -> fail (메커니증을 잘못 생각함)

n = int(input())
rgb = []
min_cost =[0]*3
for _ in range(n):
    rgb.append(list(map(int, input().split())))
min_cost[0], min_cost[1], min_cost[2] = rgb[1][0], rgb[1][1], rgb[1][2]
for i in range(1, len(rgb)):
    min_cost[0] = min_cost[0] + min(rgb[i-1][1], rgb[i-1][2])
    min_cost[1] = min_cost[1] + min(rgb[i-1][0], rgb[i-1][2])
    min_cost[2] = min_cost[2] + min(rgb[i-1][0], rgb[i-1][1])

print(min(min_cost))

# try3 -> fail (답지 시청...)

n = int(input())
rgb = []

for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, len(rgb)):
    rgb[i][0] = rgb[i][0] + min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] = rgb[i][1] + min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] = rgb[i][2] + min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2]))