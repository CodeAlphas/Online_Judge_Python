"""
 백준 23289번: 온풍기 안녕! 풀이
 Author: CodeAlphas
 Date: 2022/10/13
 Problem Source: https://www.acmicpc.net/problem/23289
 Version: Python 3.10.4
"""

import sys
import copy
from collections import deque
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(int, input().split())))

heaters = []; temperatures = []
for x in range(r):
    for y in range(c):
        if graph[x][y] in [1, 2, 3, 4]:
            heaters.append((x, y, graph[x][y]))
        elif graph[x][y] == 5:
            temperatures.append((x, y))

w = int(input())
walls = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x, y, t = map(int, input().split())
    walls[x-1][y-1].append(t)

def check(num, x, y, dir):
    global walls
    if not(0 <= x < r and 0 <= y < c): return False
    if dir == 1:
        if 1 in walls[x][y-1]: return False
        if num == 1:
            if 0 in walls[x+1][y-1]: return False
        elif num == 2:
            if 0 in walls[x][y-1]: return False
    elif dir == 2:
        if 1 in walls[x][y]: return False
        if num == 1:
            if 0 in walls[x+1][y+1]: return False
        elif num == 2:
            if 0 in walls[x][y+1]: return False
    elif dir == 3:
        if 0 in walls[x+1][y]: return False
        if num == 1:
            if 1 in walls[x+1][y]: return False
        elif num == 2:
            if 1 in walls[x+1][y-1]: return False
    else:
        if 0 in walls[x][y]: return False
        if num == 1:
            if 1 in walls[x-1][y]: return False
        elif num == 2:
            if 1 in walls[x-1][y-1]: return False
    return True

directions = [[(0, 0)],
              [(0, 1), (-1, 1), (1, 1)],
              [(0, -1), (-1, -1), (1, -1)],
              [(-1, 0), (-1, -1), (-1, 1)],
              [(1, 0), (1, -1), (1, 1)]]
def wind():
    global temper_graph
    for x, y, dir in heaters:
        temp_graph = [[0] * c for _ in range(r)]
        nx = x + directions[dir][0][0]; ny = y + directions[dir][0][1]
        if check(0, nx, ny, dir):
            t_num = 5
            queue = deque([(t_num, nx, ny, dir)])
        else: continue
        while queue:
            t_num, x, y, dir = queue.popleft()
            temp_graph[x][y] = t_num
            if t_num == 0: break
            for i in range(3):
                nx = x + directions[dir][i][0]; ny = y + directions[dir][i][1]
                if check(i, nx, ny, dir):
                    queue.append((t_num-1, nx, ny, dir))

        for x in range(r):
            for y in range(c):
                temper_graph[x][y] += temp_graph[x][y]

c_directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
def control():
    global temper_graph
    t_graph = copy.deepcopy(temper_graph)

    for x in range(r):
        for y in range(c):
            for i in range(1, 5):
                nx = x + c_directions[i][0]; ny = y + c_directions[i][1]
                if check(0, nx, ny, i):
                    if temper_graph[x][y] > temper_graph[nx][ny]:
                        t_graph[nx][ny] += (temper_graph[x][y] - temper_graph[nx][ny])//4
                        t_graph[x][y] -= (temper_graph[x][y] - temper_graph[nx][ny])//4
    temper_graph = t_graph

def decrease():
    global temper_graph
    for x in range(r):
        for y in range(c):
            if x == 0 or y == 0 or x == r-1 or y == c-1:
                if temper_graph[x][y] >= 1:
                    temper_graph[x][y] -= 1

def temper_check():
    global temperatures
    for x, y in temperatures:
        if temper_graph[x][y] >= k: continue
        else: return False
    return True

result = 0
temper_graph = [[0] * c for _ in range(r)]
while True:
    wind()
    control()
    decrease()
    result += 1
    if temper_check() or result > 100: print(result); break