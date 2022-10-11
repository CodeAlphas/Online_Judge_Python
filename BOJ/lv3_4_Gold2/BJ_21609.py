"""
 백준 21609번: 상어 중학교 풀이
 Author: CodeAlphas
 Date: 2022/10/11
 Problem Source: https://www.acmicpc.net/problem/21609
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def check(x, y, num):
    visited = [[False] * n for _ in range(n)]
    count = 1; rainbow_count = 0
    group_mem = [(x, y)]
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]; ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != -1 and visited[nx][ny] == False:
                if graph[nx][ny] == 0 or graph[nx][ny] == num:
                    if graph[nx][ny] == 0: rainbow_count += 1
                    queue.append((nx, ny))
                    group_mem.append((nx, ny))
                    count += 1
                    visited[nx][ny] = True

    return count, group_mem, rainbow_count

def find_blockgroup():
    visited = [[False] * n for _ in range(n)]
    max_count = -1; max_rainbow = -1; max_group_mem = []
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= 1 and visited[x][y] == False:
                count, group_mem, rainbow_count = check(x, y, graph[x][y])
                for i, j in group_mem:
                    if graph[i][j] >= 1: visited[i][j] = True
                if count > max_count:
                    max_count = count
                    max_group_mem = group_mem
                    max_rainbow = rainbow_count
                elif count == max_count:
                    if rainbow_count >= max_rainbow:
                        max_group_mem = group_mem
                        max_rainbow = rainbow_count

    return max_count, max_group_mem

def remove_blockgroup(max_count, max_group_mem):
    global grade
    for x, y in max_group_mem:
        graph[x][y] = -10
    grade += max_count ** 2

def gravity():
    global graph
    for x in range(n-2, -1, -1):
        for y in range(n):
            if graph[x][y] > -1:
                r = x + 1; tx = x; ty = y
                while 0 <= r < n and graph[r][y] == -10:
                    graph[tx][ty], graph[r][ty] = graph[r][ty], graph[tx][ty]
                    tx = r
                    r += 1

def rotate():
    global graph
    temp_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            temp_graph[x][y] = graph[y][n-1-x]
    graph = temp_graph

grade = 0
while True:
    max_count, max_group_mem = find_blockgroup()
    if max_count < 2:
        print(grade)
        break
    remove_blockgroup(max_count, max_group_mem)
    gravity()
    rotate()
    gravity()