
from re import search
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
timetable = []
paytable = []
N = int(input())
for _ in range(N):
  t,p = map(int,input().split())

  timetable += [t]
  paytable += [p]

MAXDAY = len(timetable)



cur_pay = 0
answer = 0

def search(today,cur_pay):
  global answer
   
  if today >= MAXDAY:
      answer = max(answer,cur_pay)
      return

  for day in range(today, MAXDAY):
    if not working[day] and (day+timetable[day]-1) < MAXDAY:


      working[day:day+timetable[day]] = [True]*timetable[day]
      cur_pay += paytable[day]

      search(day+timetable[day],cur_pay)

      working[day:day+timetable[day]] = [False]*timetable[day]
      cur_pay -= paytable[day]

# main
working = [False] * MAXDAY
for start in range(MAXDAY):
  search(start,0)


print(answer)
  
      
  
