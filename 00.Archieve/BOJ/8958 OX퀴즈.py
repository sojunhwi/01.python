# https://www.acmicpc.net/problem/8958

cnt = int(input())
board = list(range(cnt))
for i in range(cnt):
    score = 0
    board[i] = score
    case = input()
    for j in range(len(case)):
        if case[j] == 'O':
            score += 1
            board[i] += score
        elif case[j] == 'X':
            score = 0
    print(board[i])


