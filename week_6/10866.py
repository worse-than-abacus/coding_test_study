from collections import deque
import sys

def push_front(x, deq) :
    deq.appendleft(x)
    return deq

def push_back(x, deq) :
    deq.append(x)
    return deq

def pop_front(deq) :
  if deq : return print(deq.popleft())
  else: return print(-1)

def pop_back(deq) :
  if deq : return print(deq.pop())
  else: return print(-1)

def size(deq) :
  return print(len(deq))

def empty(deq) :
  if len(deq) >= 1: return print(0)
  else : return print(1)

def front(deq) :
  if len(deq) >= 1: return print(deq[0])
  else : return print(-1)

def back(deq) :
  if len(deq) >= 1 : return print(deq[-1])
  else : return print(-1)

statements_dic = {
    'push_front' : push_front ,
    'push_back' : push_back,
    'pop_front' : pop_front,
    'pop_back' : pop_back,
    'size' : size,
    'empty' : empty,
    'front' : front,
    'back' : back
}

deq = deque()
for i in range(int(sys.stdin.readline())) :
  statement = sys.stdin.readline().split()

  if len(statement)==1 :
    cmd = statement[0]
    statements_dic[cmd](deq)
  else :
    cmd ,x = statement
    statements_dic[cmd](x,deq)