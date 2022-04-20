n = int(input())
signs = list(map(str,input().split()))
min = ''
max = ''
check_list = [False] * 10
def check(i,j,k):
    if k == '>':
        return i>j # return True or False
    else :
        return i<j # return True or False


def solution(cnt,s):
    global min, max
    if cnt > n :
        if len(min) == 0 :
            min = s
        else : max = s
        return

    for i in range(10):
        if check_list[i] == False :
            if cnt ==0 or check(s[-1], str(i), signs[cnt-1]):
                check_list[i] = True
                solution(cnt+1,s+str(i))
                check_list[i] = False

solution(0,'')
print(max)
print(min)