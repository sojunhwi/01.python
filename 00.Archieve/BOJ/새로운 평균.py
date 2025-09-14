import sys

cnt=int(sys.stdin.readline())
score=list(map(int,sys.stdin.readline().split()))
total=0
max_score=sorted(score)[cnt-1]

for i in range(cnt):
    score[i]=(score[i]/max_score)*100
    total=total+score[i]
print("%.2f"%(total/cnt))


