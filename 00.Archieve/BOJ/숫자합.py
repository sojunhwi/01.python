#더할 숫자 갯수
count=int(input())
#더할 숫자들
num=input()
#더한 숫자 넣을 변수
total=0
#숫자 갯수만큼 반복해서 숫자 더하기
for i in range(count):
    total=total+int(num[i])

print(total)
