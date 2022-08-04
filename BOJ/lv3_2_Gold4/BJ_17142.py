"""
 백준 17142번: 연구소 3 풀이
 Author: CodeAlphas
 Date: 2022/07/15
 Problem Source: https://www.acmicpc.net/problem/17142
 Version: Python 3.10.4
"""

import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maps = []; viruses = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

for x in range(n):
    for y in range(n):
        if maps[x][y] == 2:
            viruses.append((x, y))

comb_virus = list(combinations(viruses, m))
INF = int(1e10)
result = INF

def check(t_maps, virus):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * n for _ in range(n)] 
    queue = deque(list(virus))
    for x, y in virus:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + move[i][0]; ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if t_maps[nx][ny] != 1:
                    queue.append((nx, ny))
                    t_maps[nx][ny] = t_maps[x][y] + 1
                    visited[nx][ny] = True
    
    time = -1
    for x in range(n):
        for y in range(n):
            if t_maps[x][y] == 0:
                return INF
            elif maps[x][y] != 2 or (x, y) in virus:
                time = max(time, t_maps[x][y])
    return time - 2

for virus in comb_virus:
    t_maps = copy.deepcopy(maps)
    result = min(result, check(t_maps, virus))

if result == INF:
    print(-1)
else:
    print(result)