H, M = map(int, input().split())

if M <= 44:
    if H == 0:
        H = 23
    elif H>0 and H<=23:
        H -=1
    M += 15
elif M>=45 and M<60:
    M -=45


print(H, M)
