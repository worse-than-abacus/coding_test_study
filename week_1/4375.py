# try1 -> 시간초과

import sys
input = sys.stdin.readline

n = int(input())
Searching = True
isFind = False
i = 0

while Searching:
  i += 1
  number = n*i
  for num in str(number):
    if num == '1':
      isFind = True
    else:
      isFind = False
      break
  
  if isFind:
    Searching = False

    
print(len(str(number)))
  

# try2 try - except을 입력 받기
import sys
input = sys.stdin.readline
while True:
  try:
    n = int(input())
  except:
    break
  number = 0
  while True:
    number = number*10 + 1
  
    if number%n == 0:
      print(len(str(number)))
      break