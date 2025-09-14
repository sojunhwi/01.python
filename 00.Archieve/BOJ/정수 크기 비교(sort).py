'''
import sys

a,b,c=map(int,sys.stdin.readline().split())

if a>=b and c>=a:
    print(a)
elif a>=c and b>=a:
    print(a)
elif b>=a and c>=b:
    print(b)
elif b>=c and a>=b:
    print(b)
elif c>=a and b>=c:
    print(c)
elif c>=b and a>=c:
    print(c)
'''

n=map(int,input().split())
print(sorted(n)[1])
# sort는 안됨 map어쩌구 오류
#print(n.sort(reverse=True))
