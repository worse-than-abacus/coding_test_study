#try 1
import sys
input = sys.stdin.readline

l,c = map(int,input().split())
eng_char = sorted(input().split())
visited = [False] * c

def search(res,start_idx):
  global l,eng_char
  if len(res) == l:
    print(''.join(res))
    return

  for i in range(start_idx,len(eng_char)):
    if not visited[i]:
      visited[i] = True
      res.append(eng_char[i])
      search(res,start_idx+1)
      res.pop()
      visited[i] = False
    
for i in range(len(eng_char)):
  visited[i] = True
  search([eng_char[i]],i+1)
  visited[i] = False

# try 2 -> 성공
import sys
input = sys.stdin.readline

l,c = map(int,input().split())
eng_char = sorted(input().split())
visited = [False] * c
m_chars = ["a", "e", "i", "o", "u"]
s_chars = list(set(eng_char)-set(m_chars))

def search(res,start_idx):
  global l,eng_char
  if len(res) == l:
    m_cnt, s_cnt = 0, 0
    for m_char in m_chars:
      if m_char in res:
        m_cnt += 1

    for s_char in s_chars:
      if s_char in res:
        s_cnt += 1

    if m_cnt >=1 and s_cnt >=2:
      print(''.join(res))
      return
    return

  for i in range(start_idx,len(eng_char)):
    if not visited[i]:
      visited[i] = True
      res.append(eng_char[i])
      search(res,i+1)
      res.pop()
      visited[i] = False
    
for start in range(len(eng_char)):
  visited[start] = True
  search([eng_char[start]],start+1)
  visited[start] = False