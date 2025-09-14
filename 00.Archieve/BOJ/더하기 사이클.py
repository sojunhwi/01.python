ini=input()
cnt=0
num=ini
fin=''
if len(ini)==1:
    num='0'+num
    ini='0'+ini
    
while ini!=fin:
    num=num[1]+str((int(num[0])+int(num[1]))%10)
    cnt+=1
    fin=num
print(cnt)
    
    
