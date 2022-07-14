"""
 백준 2638번: 치즈 풀이
 Author: CodeAlphas
 Date: 2022/06/24
 Problem Source: https://www.acmicpc.net/problem/2638
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]; time = 0

def check(x, y, maps, visited):
    queue = deque([(x, y)])
    visited[x][y] = True; temp = []

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + moves[i][0]; ny = y + moves[i][1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    maps[nx][ny] += 1
                    temp.append((nx, ny))

    for x, y in temp:
        if maps[x][y] >= 3:
            maps[x][y] = 0
        elif maps[x][y] == 2:
            maps[x][y] = 1
    return maps

while True:
    ch = False; visited = [[False] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if maps[x][y] == 1:
                ch = True; break
    if ch:
        time += 1
        maps = check(x, y, maps, visited)
    else:
        print(time); break
