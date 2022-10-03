"""
 백준 2580번: 스도쿠 풀이
 Author: CodeAlphas
 Date: 2022/10/03
 Problem Source: https://www.acmicpc.net/problem/2580
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

zeroes = []
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            zeroes.append((x, y))
z_n = len(zeroes)

def check(board, x, y, num):

    for i in range(9):
        if board[i][y] == num or board[x][i] == num:
            return False
    
    st_x = x // 3 * 3; st_y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[st_x + i][st_y + j] == num: return False
    return True

def dfs(iter):
    global board, zeroes

    if iter == z_n:
        for i in range(9):
            print(*board[i])
        exit(0)

    x, y = zeroes[iter][0], zeroes[iter][1]
    for num in range(1, 10):
        if check(board, x, y, num):
            board[x][y] = num
            dfs(iter+1)
            board[x][y] = 0

dfs(0)