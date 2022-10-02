"""
 백준 19236번: 청소년 상어 풀이
 Author: CodeAlphas
 Date: 2022/10/02
 Problem Source: https://www.acmicpc.net/problem/19236
 Version: Python 3.10.4
"""

import sys
import copy
input = sys.stdin.readline

direction = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
graph = []; fishes = {}; result = 0
for i in range(1, 16):
    fishes[i] = 0

for i in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    graph.append([[a, b], [c, d], [e, f], [g, h]])
    fishes[a] = [b, i, 0]
    fishes[c] = [d, i, 1]
    fishes[e] = [f, i, 2]
    fishes[g] = [h, i, 3]

def f_move(graph, fishes, s_x, s_y):
    t_fishes = copy.deepcopy(fishes)

    for num in t_fishes:
        dir, x, y = fishes[num]

        for _ in range(8):
            nx = x + direction[dir][0]; ny = y + direction[dir][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx != s_x or ny != s_y):
                n_num, n_dir = graph[nx][ny]
                graph[x][y] = [n_num, n_dir]; fishes[n_num] = [n_dir, x, y]
                graph[nx][ny] = [num, dir]; fishes[num] = [dir, nx, ny]
                break
            else: 
                dir += 1; dir %= 9 
                if dir == 0: dir = 1
    return graph, fishes


def dfs(x, y, eat, graph, fishes):
    global result

    n = graph[x][y][0]; s_dir = graph[x][y][1]
    del fishes[n]; graph[x][y] = [0, 0]
    eat += n 

    graph, fishes = f_move(graph, fishes, x, y)

    ch = True
    for _ in range(3):
        nx = x + direction[s_dir][0]; ny = y + direction[s_dir][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny] != [0, 0]:
            dfs(nx, ny, eat, copy.deepcopy(graph), copy.deepcopy(fishes))
            ch = False
        x = nx; y = ny
    
    if ch:
        result = max(eat, result)
        return

dfs(0, 0, 0, graph, fishes)
print(result)