T =  int(input())

arr =[[0] for _ in range(1_000_001)]

arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4,1_000_001):
    arr[i] = (arr[i-1]+arr[i-2]+arr[i-3])%1000000009


for _ in range(T):
    print(arr[int(input())])