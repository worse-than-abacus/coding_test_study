def make_only_num1(n):
    num = 1

    while True:
        remainder = num%n 
        if remainder != 0 :
            num = num*10 + 1
        else : 
            str_num = str(num)
            print(len(str_num))
            break

n = int(input())
make_only_num1(n)

#### fail,,, 예전에 봤던 답지를 토대로 했는데 틀렸다...
#### try와 except를 사용해야한다... 왜지??

def make_only_num1(n):
    num = 1

    while True:
        remainder = num%n 
        if remainder != 0 :
            num = num*10 + 1
        else : 
            str_num = str(num)
            print(len(str_num))
            break
while True:
    try:
        n = int(input())
        make_only_num1(n)
    except:
        break

#### success