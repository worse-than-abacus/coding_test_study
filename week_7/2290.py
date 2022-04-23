# try 1 -> 성공
import sys
input = sys.stdin.readline

s, numbers = map(int,input().split())
numbers = str(numbers)

barv_right = [" "]*(s+1)+["|"] +[" "]
barv_left = ["|"]+[" "]*(s+1) +[" "]
barv_double = ["|"]+[" "]*s+["|"] +[" "]
barh = [" "]+["-"]*s+[" "] +[" "]
row_space = [" "]*(s+2) +[" "]

table = [[] for _ in range(s*2+3)]

num1 = [
  row_space,
  barv_right,
  row_space,
  barv_right,
  row_space
]


num2 = [
  barh,
  barv_right,
  barh,
  barv_left,
  barh
]

num3 = [
  barh,
  barv_right,
  barh,
  barv_right,
  barh
]

num4 = [
  row_space,
  barv_double,
  barh,
  barv_right,
  row_space
]

num5 = [
  barh,
  barv_left,
  barh,
  barv_right,
  barh
]

num6 = [
  barh,
  barv_left,
  barh,
  barv_double,
  barh
]

num7 = [
  barh,
  barv_right,
  row_space,
  barv_right,
  row_space
]

num8 = [
  barh,
  barv_double,
  barh,
  barv_double,
  barh
]

num9 = [
  barh,
  barv_double,
  barh,
  barv_right,
  barh
]

num0 = [
  barh,
  barv_double,
  row_space,
  barv_double,
  barh
]

def remove_last_space():
  global table
  for row_idx in range(s*2+3):
    table[row_idx].pop()

def print_num(input_array):
  global table,s
  row_idx = 0
  for row in input_array:
    cnt = 0
    if "|" in row: 
      while cnt < s:
        table[row_idx].extend(row)
        row_idx += 1
        cnt += 1        
    else:
      table[row_idx].extend(row)
      row_idx += 1

for num in numbers:
  if num == "1":
    print_num(num1)
  elif num == "2":
    print_num(num2)
  elif num == "3":
    print_num(num3)
  elif num == "4":
    print_num(num4)
  elif num == "5":
    print_num(num5)
  elif num == "6":
    print_num(num6)
  elif num == "7":
    print_num(num7)
  elif num == "8":
    print_num(num8)
  elif num == "9":
    print_num(num9)
  elif num == "0":
    print_num(num0)
    
remove_last_space()
for row in table:
  print(''.join(row))