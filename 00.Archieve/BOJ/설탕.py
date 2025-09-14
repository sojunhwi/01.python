weight=int(input())
sugar=0

while weight>0:
    if weight%5==0:
        sugar+=1
        weight-=5
    elif weight%5!=0:
        sugar+=1
        weight-=3
        if weight<0:
            sugar=-1
            break
#없어도됨
'''
    elif weight%5!=0 and weight%3!=0:
        sugar=-1
'''            
print(sugar)
