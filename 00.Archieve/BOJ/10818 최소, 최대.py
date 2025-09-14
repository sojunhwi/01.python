# https://www.acmicpc.net/problem/10818

from sys import stdin as std

cnt = int(std.readline())
a = std.readline().split()

for i in range(cnt):
    a[i] = int(a[i])

print(min(a),max(a))



