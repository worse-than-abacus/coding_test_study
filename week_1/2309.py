# try1
import sys
input = sys.stdin.readline
numbers = []
for _ in range(9):
  num = int(input())
  numbers += [num]
  
numbers.sort()
def findreal(numbers):
  totalsum = sum(numbers)
  for i in range(9):
    for j in range(i,9):
      if totalsum - (numbers[i]+numbers[j]) == 100:
        for num in numbers:
          if num not in [numbers[i],numbers[j]]:
            print(num)
        return
            
findreal(numbers)
