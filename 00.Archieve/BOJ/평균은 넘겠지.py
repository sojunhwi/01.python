import sys

cnt=int(sys.stdin.readline())


for i in range(cnt):
    total=0
    num=0
    List=list(map(int,sys.stdin.readline().split()))
    for i in range(1,List[0]+1):
        total+=List[i]
    total=total/List[0]
    for j in range(1,List[0]+1):
        if List[j]>total:
            num+=1
    print("%2.3f%%"%(num/List[0]*100))
