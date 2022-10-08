"""
 백준 20057번: 마법사 상어와 토네이도 풀이
 Author: CodeAlphas
 Date: 2022/10/08
 Problem Source: https://www.acmicpc.net/problem/20057
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ratios = [[(-2, 0, 2), (-1, -1, 10), (-1, 0, 7), (-1, 1, 1), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2)],
         [(-1, -1, 1), (-1, 1, 1), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 10), (1, 1, 10), (2, 0, 5)],
         [(-2, 0, 2), (-1, -1, 1), (-1, 0, 7), (-1, 1, 10), (0, 2, 5), (1, -1, 1), (1, 0, 7), (1, 1, 10), (2, 0, 2)],
         [(-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1)]]

visited = [[False] * n for _ in range(n)]
def move_tornado(x, y, dir):
    nx = x + direction[dir][0]; ny = y + direction[dir][1]
    if visited[nx][ny] == True:
        if dir == 0: dir = 3
        else: dir -= 1
        nx = x + direction[dir][0]; ny = y + direction[dir][1]
    visited[nx][ny] = True
    return nx, ny, dir

def check(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else: return False

def move_sand(x, y, dir):
    global result, sand
    temp = 0
    for dx, dy, ratio in ratios[dir]:
        nx = x + dx; ny = y + dy
        if check(nx, ny): sand[nx][ny] += int(sand[x][y] * ratio * 0.01)
        else: result += int(sand[x][y] * ratio * 0.01)
        temp += int(sand[x][y] * ratio * 0.01)

    nx = x + direction[dir][0]; ny = y + direction[dir][1]
    if check(nx, ny): sand[nx][ny] = sand[nx][ny] + sand[x][y] - temp
    else: result += sand[x][y] - temp
    sand[x][y] = 0

x = n//2; y = n//2
visited[x][y] = True
result = 0; dir = 0
while x != 0 or y != 0:
    nx, ny, dir = move_tornado(x, y, dir)
    if sand[nx][ny] != 0:
        move_sand(nx, ny, dir)
    dir += 1; dir %= 4
    x = nx; y = ny

print(result)