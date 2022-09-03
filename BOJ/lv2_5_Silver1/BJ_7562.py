"""
 백준 7562번: 나이트의 이동 풀이
 Author: CodeAlphas
 Date: 2022/09/03
 Problem Source: https://www.acmicpc.net/problem/7562
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

def check(i, x, y, tx, ty):
    visited = [[False] * i for _ in range(i)]

    queue = deque([(x, y, 0)])
    while queue:
        x, y, count = queue.popleft()
        visited[x][y] = True
        if x == tx and y == ty:
            return count
        else: 
            for move in moves:
                nx = x + move[0]; ny = y + move[1]
                if 0 <= nx < i and 0 <= ny < i and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count+1))

while t:
    i = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    result = check(i, x, y, tx, ty)
    print(result)
    t -= 1