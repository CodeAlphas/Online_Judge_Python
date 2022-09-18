"""
 백준 17822번: 원판 돌리기 풀이
 Author: CodeAlphas
 Date: 2022/09/18
 Problem Source: https://www.acmicpc.net/problem/17822
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, t = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

def rotate(x, d, k):
    global maps
    x -= 1

    if d == 0:
        while k:
            temp = maps[x].pop()
            maps[x].insert(0, temp)
            k -= 1
    else:
        while k:
            temp = maps[x].pop(0)
            maps[x].append(temp)
            k -= 1

def remove(i, j, visited):
    global maps
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num = maps[i][j]; result = 0

    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + moves[k][0]; ny = y + moves[k][1]
            if ny < 0:
                ny = m-1
            elif ny >= m:
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and maps[nx][ny] == num:
                visited[nx][ny] = True
                queue.append((nx, ny))
                maps[nx][ny] = -10
                result = 1

    if result == 1:
        maps[i][j] = -10
    return result

def find():
    global maps
    visited = [[False] * m for _ in range(n)]
    rm_count = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] != -10:
                rm_count += remove(i, j, visited)
    
    if rm_count == 0:
        c = 0; sum_n = 0
        for i in range(n):
            for j in range(m):
                if maps[i][j] != -10:
                    sum_n += maps[i][j]
                    c += 1
        if c != 0:
            aver_n = sum_n / c
            for i in range(n):
                for j in range(m):
                    if maps[i][j] != -10:
                        if maps[i][j] > aver_n:
                            maps[i][j] -= 1
                        elif maps[i][j] < aver_n:
                            maps[i][j] += 1

while t:
    t -= 1
    x, d, k = map(int, input().split())
    x_ = x

    while x <= n:
        rotate(x, d, k)
        x += x_        
    find()

result = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] != -10:
            result += maps[i][j]

print(result)