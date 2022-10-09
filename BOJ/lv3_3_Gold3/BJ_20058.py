"""
 백준 20058번: 마법사 상어와 파이어스톰 풀이
 Author: CodeAlphas
 Date: 2022/10/09
 Problem Source: https://www.acmicpc.net/problem/20058
 Version: Python 3.10.4
"""

# PyPy3 통과
import sys
import copy
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
ices = []
n = 2**n
for _ in range(n):
    ices.append(list(map(int, input().split())))

stages = list(map(int, input().split()))

def rotate(ix, iy, il, t_ices):
    global ices
    for x in range(ix, ix+il):
        for y in range(iy, iy+il):
            ices[x][y] = t_ices[il-1-y+iy+ix][x+iy-ix]

def divide(l):
    l = 2**l
    t_ices = copy.deepcopy(ices)
    for x in range(0, n, l):
        for y in range(0, n, l):
            rotate(x, y, l, t_ices)

def check(x, y):
    if 0 <= x < n and 0 <= y < n: return True
    else: return False

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def remove():
    global ices
    t_ices = copy.deepcopy(ices)
    for x in range(n):
        for y in range(n):
            count = 0
            if ices[x][y] != 0:
                for i in range(4):
                    nx = x + direction[i][0]; ny = y + direction[i][1]
                    if check(nx, ny) and ices[nx][ny] != 0: count += 1
                if count < 3:
                    t_ices[x][y] -= 1
    ices = t_ices

visited = [[False] * n for _ in range(n)]
def bfs(x, y):
    global ices, visited, max_count
    count = 1
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]; ny = y + direction[i][1]
            if check(nx, ny) and visited[nx][ny] == False and ices[nx][ny] != 0:
                count += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    max_count = max(max_count, count)

for l in stages:
    divide(l)
    remove()

remain_ices = 0
for x in range(n):
    for y in range(n):
        remain_ices += ices[x][y]
print(remain_ices)

max_count = 0
for x in range(n):
    for y in range(n):
        if ices[x][y] != 0 and visited[x][y] == False:
            bfs(x, y)
print(max_count)