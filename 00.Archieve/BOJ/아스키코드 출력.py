#아스키코드
num=input()

List='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#0 48
#A 65
#a 97
Result=List.find(num)
if Result<10:
    print(Result+48)
elif Result<36:
    print(Result+55)
else: print(Result+61)


#내장함수로 출력
#print(ord(input()))
