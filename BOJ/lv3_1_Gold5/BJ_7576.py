"""
 백준 7576번: 토마토 풀이
 Author: CodeAlphas
 Date: 2022/06/04
 Problem Source: https://www.acmicpc.net/problem/7576
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split()) # 상자의 가로 칸의 수,  상자의 세로 칸의 수
tomatoes = []; days = 0

for _ in range(n):
    tomatoes.append(list(map(int, input().split())))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

queue = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

def check():

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move[i][0]; ny = y + move[i][1] 
            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx, ny))

check()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()
        else:
            days = max(days, tomatoes[i][j])

print(days - 1)


    

