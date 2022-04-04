E, S, M = map(int,input().split())

n = 1
while True:
  if ((n-E)%15 == 0)and((n-S)%28 == 0) and((n-M)%19 == 0):
    print(n)
    break
  else : n +=1