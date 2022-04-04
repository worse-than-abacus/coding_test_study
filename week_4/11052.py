n = int(input())
cost_list = [0]
cost_list.extend(list(map(int,input().split())))

T_cost=[0]*(n+1)

for i in range(1,n+1):
  for j in range(1,i+1):
    T_cost[i] = max(T_cost[i],T_cost[i-j]+cost_list[j])

print(T_cost[n])