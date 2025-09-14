word=input().upper()
Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cnt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(26):
    cnt[i]=word.count(Alphabet[i])

if cnt.count(max(cnt))>1:
    print('?')
else:
    print(Alphabet[cnt.index(max(cnt))])


    
