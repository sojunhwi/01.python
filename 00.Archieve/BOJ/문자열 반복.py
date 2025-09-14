cnt=int(input())

for i in range(cnt):
    cnt_str=input()
    STR=''
    for j in range(2,len(cnt_str)):
        STR+=cnt_str[j]*int(cnt_str[0])
    print(STR)
