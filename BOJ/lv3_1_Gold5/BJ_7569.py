"""
 백준 7569번: 토마토 풀이
 Author: CodeAlphas
 Date: 2022/05/25
 Problem Source: https://www.acmicpc.net/problem/7569
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

m, n, h = map(int, input().split())

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

tomatoes = [[] for _ in range(h)]
h_ = -1

for i in range(n*h):
    if i % n == 0:
        h_ += 1
    tomatoes[h_].append(list(map(int, input().split())))

def bfs():

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]; ny = y + dy[i]; nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomatoes[nz][nx][ny] == 0: # 순서 주의 tomatoes[nz][nx][ny] == 0이 맨 앞으로가면 오류
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                queue.append((nx, ny, nz))
    
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomatoes[z][x][y] == 1:
                queue.append((x, y, z))

bfs()

timer = 1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomatoes[z][x][y] == 0:
                print(-1)
                exit()
            else:
                timer = max(timer, tomatoes[z][x][y])

print(timer-1)