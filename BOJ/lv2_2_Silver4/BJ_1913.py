"""
 백준 1913번: 달팽이 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/1913
 Version: Python 3.10.4
"""

n = int(input())
m = int(input())

# 아래, 왼쪽, 위, 오른쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maps = [[0] * n for _ in range(n)]
v = n * n
x = 0; y = 0; i = 0

while(v):
    maps[x][y] = v
    if v == 1:
        break
    v -= 1
    while(True):
        nx = x + dx[i]; ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or maps[nx][ny] != 0:
            i = (i + 1) % 4
            continue
        x = nx; y = ny
        break

for i in range(n):
    for j in range(n):
        print(maps[i][j], end = ' ')
        if maps[i][j] == m:
            x = i; y = j
    print()

print(x+1, y+1)