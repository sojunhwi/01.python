from sys import stdin as std
c = []
d = []
a = 1
b = 2
while a ==True:
    a, b = map(int, std.readline().split())
    c.append(a)
    d.append(b)
    print(c,d)
    print(bool(a),bool(b))

for i in range(len(c)-1):
    print(c[i]+d[i])


