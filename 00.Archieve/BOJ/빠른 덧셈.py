import sys
cnt=int(sys.stdin.readline())
a=list(range(cnt))
b=list(range(cnt))

for i in range(cnt):
    a[i],b[i]=map(int,sys.stdin.readline().split())

for i in range(cnt):
    print(a[i]+b[i])


