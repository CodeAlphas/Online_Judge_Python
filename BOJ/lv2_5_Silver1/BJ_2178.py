"""
 백준 2178번: 미로 탐색 풀이
 Author: CodeAlphas
 Date: 2022/06/11
 Problem Source: https://www.acmicpc.net/problem/2178
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline


move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maps = []

n, m = map(int, input().split())

for _ in range(n):
    maps.append(list(map(int, list(input().rstrip()))))

def check():
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + move[i][0]; ny = y + move[i][1]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
        
check()
print(maps[n-1][m-1])