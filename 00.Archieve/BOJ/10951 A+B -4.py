from sys import stdin as std

while True:
    try:
        a, b = map(int,std.readline().split())
        print(a+b)
    except:
        break

##for line in std:
##    a, b = map(int, line.split())
##    print(a+b)
        
