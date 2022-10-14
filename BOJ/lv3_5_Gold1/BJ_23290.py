"""
 백준 23290번: 마법사 상어와 복제 풀이
 Author: CodeAlphas
 Date: 2022/10/14
 Problem Source: https://www.acmicpc.net/problem/23290
 Version: Python 3.10.4
"""

import sys
import copy
input = sys.stdin.readline

m, s = map(int, input().split())
graph = [[[0] * 9 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x-1][y-1][d] += 1

sx, sy = map(int, input().split())
sx -= 1; sy -= 1

def check(x, y):
    global fish_smell
    if not (0 <= x < 4 and 0 <= y < 4): return False
    if x == sx and y == sy: return False
    if fish_smell[x][y] > 0: return False
    return True

f_direction = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
def fish_move(t_graph):
    global graph
    for x in range(4):
        for y in range(4):
            for i in range(1, 9):
                temp = t_graph[x][y][i]
                if temp > 0:
                    while temp:
                        d = i
                        for _ in range(8):
                            nx = x + f_direction[d][0]; ny = y + f_direction[d][1]
                            if check(nx, ny):
                                graph[x][y][i] -= 1
                                graph[nx][ny][d] += 1
                                break
                            else:
                                if d == 1: d = 8
                                else: d -= 1
                        temp -= 1

s_direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def shark_move(x, y, count, visited, depth):
    global max_count, max_fishes, max_x, max_y

    if depth == 3:
        if count > max_count:
            max_count = count
            max_fishes = visited[:]
            max_x = x; max_y = y
        return

    for dx, dy in s_direction:
        nx = x + dx; ny = y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            temp = sum(graph[nx][ny])
            if (nx, ny) not in visited and temp > 0:
                visited.append((nx, ny))
                shark_move(nx, ny, count + temp, visited, depth + 1)
                visited.pop()
            else:
                shark_move(nx, ny, count, visited, depth + 1)
    return

def remove_smell():
    global fish_smell
    for x in range(4):
        for y in range(4):
            if fish_smell[x][y] > 0:
                fish_smell[x][y] -= 1

def finish_copy(t_graph):
    global graph
    for x in range(4):
        for y in range(4):
            for i in range(9):
                graph[x][y][i] += t_graph[x][y][i]

fish_smell = [[0] * 4 for _ in range(4)]
for _ in range(s):
    t_graph = copy.deepcopy(graph)
    fish_move(t_graph)

    max_count = -1; max_fishes = []; max_x = sx; max_y = sy
    shark_move(sx, sy, 0, [], 0)

    for x, y in max_fishes:
        graph[x][y] = [0] * 9
        fish_smell[x][y] = 3
    sx = max_x; sy = max_y

    remove_smell()
    finish_copy(t_graph)
    s -= 1

result = 0
for x in range(4):
    for y in range(4):
        result += sum(graph[x][y])
print(result)