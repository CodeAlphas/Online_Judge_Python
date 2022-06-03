"""
 백준 2667번: 단지번호붙이기 풀이
 Author: CodeAlphas
 Date: 2022/05/27
 Problem Source: https://www.acmicpc.net/problem/2667
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = []
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    maps.append(list(map(int, list(input().rstrip()))))

def bfs(x, y):
    queue = deque([(x, y)])
    maps[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dir[i][0]; ny = y + dir[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = 0
                count += 1

    return count

counts = []; ans = 0   
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            ans += 1
            count = bfs(i, j)
            counts.append(count)

print(ans)
counts.sort()
for count in counts:
    print(count)