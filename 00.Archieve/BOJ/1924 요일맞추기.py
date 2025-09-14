day=['SUN','MON','TUE','WED','THU','FRI','SAT']
month=[31,28,31,30,31,30,31,31,30,31,30,31]

#월 일 입력
mon,dat=input().split()
#문자->정수
mon=int(mon)
dat=int(dat)
#요일 계산할 일수
date=0

#전월까지 일수 합
for i in range(0,mon-1):
    date=date+month[i]

#해당 일 더하기
date+=dat

#7로 나누면 요일나옴
print(day[date%7])
