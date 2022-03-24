while True:
  try : 
      n=int(input())
  except EOFError:
      break
  a,b='1',1
  while int(a*b)%n!=0:
    b+=1
  print(b)