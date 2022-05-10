t = int(input())
for _ in range(t):
    n = int(input())

    d=[0]*(n+1)
    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, len(d)):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[-1])

#try1 -> fail (over memory)

t = int(input())
for _ in range(t):
    n = int(input())

    d=[0]*(n+1)
    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, len(d)):
        d[i] = (d[i-1] + d[i-2] + d[i-3])%1000000009

    print(d[-1])

# try2 -> fail (over time)

d= [0] * 1000001
d[1], d[2], d[3] = 1, 2, 4

for i in range(4, 1000001):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

for _ in range(int(input())):
    n = int(input())
    print(d[n])

# sucess
