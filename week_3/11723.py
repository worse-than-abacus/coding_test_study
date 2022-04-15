import sys
input = sys.stdin.readline
n=int(input())
S=set()
for _ in range(n):
  cmd = input().split()
  if len(cmd) == 1 :
    if cmd[0] == 'all':
      S = set(range(1,21))
    else :
      S= set()
  else:
    cmd[1] = int(cmd[1])
    if cmd[0] == 'add':
      S.add(cmd[1])
    elif cmd[0] == 'remove':
      S.discard(cmd[1])
    elif cmd[0] == 'check':
      print(1 if cmd[1] in S else 0)
    elif cmd[0] == 'toggle':
      if cmd[1] in S :
        S.discard(cmd[1])
      else :
        S.add(cmd[1])