"""
 백준 19237번: 어른 상어 풀이
 Author: CodeAlphas
 Date: 2022/10/04
 Problem Source: https://www.acmicpc.net/problem/19237
 Version: Python 3.10.4
"""

import sys
import copy

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]
for x in range(n):
    temp = list(map(int, input().split()))
    for y in range(n):
        num = temp.pop(0)
        if num != 0: graph[x][y].append(num)

s_directions = [0] + list(map(int, input().split()))
sharks = []
smell_graph = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        smell_graph[x][y] = []
        if graph[x][y] != []:
            sharks.append([graph[x][y][0], x, y, s_directions[graph[x][y][0]]])

directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
priorities = [[] for _ in range(m + 1)]
for num in range(1, m + 1):
    for _ in range(4):
        priorities[num].append(tuple(map(int, input().split())))

def move():
    global graph, sharks, smell_graph, time
    t_shark = copy.deepcopy(sharks)
    
    for num, x, y, dir in t_shark:
        smell_graph[x][y] = [num, k]

    for num, x, y, dir in t_shark:
        ch = True
        for i in range(4):
            n_dir = priorities[num][dir - 1][i]
            nx = x + directions[n_dir][0]
            ny = y + directions[n_dir][1]
            if 0 <= nx < n and 0 <= ny < n and smell_graph[nx][ny] == []:
                sharks.remove([num, x, y, dir]); graph[x][y].remove(num)
                sharks.append([num, nx, ny, n_dir]); graph[nx][ny].append(num)
                ch = False
                break
        if ch:
            for i in range(4):
                n_dir = priorities[num][dir - 1][i]
                nx = x + directions[n_dir][0]
                ny = y + directions[n_dir][1]
                if 0 <= nx < n and 0 <= ny < n and smell_graph[nx][ny][0] == num:
                    sharks.remove([num, x, y, dir]); graph[x][y].remove(num)
                    sharks.append([num, nx, ny, n_dir]); graph[nx][ny].append(num)
                    break

    for x in range(n):
        for y in range(n):
            if smell_graph[x][y] != []:
                s_n = smell_graph[x][y][0]
                s_t = smell_graph[x][y][1]
                if s_t - 1 > 0:
                    smell_graph[x][y] = [s_n, s_t - 1]
                else:
                    smell_graph[x][y] = []

def check():
    global graph, sharks, smell_graph
    t_shark = copy.deepcopy(sharks)

    for x in range(n):
        for y in range(n):
            if len(graph[x][y]) > 1:
                live = min(graph[x][y])
                for num, sh_x, sh_y, dir in t_shark:
                    if sh_x == x and sh_y == y and num != live:
                        sharks.remove([num, sh_x, sh_y, dir])
                        graph[x][y].remove(num)

time = 0
while True:

    move()
    time += 1
    if time > 1000:
        time = -1
        break

    check()
    if len(sharks) == 1:
        break

print(time)