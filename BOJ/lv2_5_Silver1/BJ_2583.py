"""
 백준 2583번: 영역 구하기 풀이
 Author: CodeAlphas
 Date: 2022/08/29
 Problem Source: https://www.acmicpc.net/problem/2583
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
maps = [[1] * n for _ in range(m)]
for _ in range(k):
    a, b, c, d = map(int, input().split())
    b = m - b
    d = m - d

    for x in range(d, b):
        for y in range(a, c):
            maps[x][y] = 0

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def check(x, y):
    global maps

    queue = deque([(x, y)])
    count = 1; maps[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx = x + dx; ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = 0
                count += 1

    return count

result = []
for x in range(m):
    for y in range(n):
        if maps[x][y] == 1:
            result.append(check(x, y))
result.sort()

print(len(result))
print(*result)