import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = []

def foo(start):
  if len(s) == m:
    print(*s)
    return

  for i in range(start,n+1):
    if  i in s:
      continue
    
    s.append(i)
    foo(i+1)
    s.pop()
    
foo(1)