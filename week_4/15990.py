T =  int(input())

arr =[[0,0,0] for _ in range(100001)]

arr[1] = [1,0,0]
arr[2] = [0,1,0]
arr[3] = [1,1,1]

for i in range(4,100001):
    arr[i][0] = arr[i-1][1]%1000000009 + arr[i-1][2]%1000000009
    arr[i][1] = arr[i-2][0]%1000000009 + arr[i-2][2]%1000000009
    arr[i][2] = arr[i-3][0]%1000000009 + arr[i-3][1]%1000000009

for _ in range(T):
    print(sum(arr[int(input())])%1000000009)