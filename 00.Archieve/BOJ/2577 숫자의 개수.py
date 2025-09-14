#https://www.acmicpc.net/problem/2577

a = input()
b = input()
c = input()

total = int(a) * int(b) * int(c)
total = str(total)
cnt = list(range(10))
for i in range(10):
    cnt[i] = total.count(str(i))
    print(cnt[i])





# # 1~9 대입
# for i in range(10):
#     # 각 자릿수와 비교
#     cnt = 0
#     for j in range(len(total)):
#         if total[j] == str(i):
#             cnt += 1

#     print(cnt)


