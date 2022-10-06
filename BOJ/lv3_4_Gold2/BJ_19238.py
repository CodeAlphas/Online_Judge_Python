"""
 백준 19238번: 스타트 택시 풀이
 Author: CodeAlphas
 Date: 2022/10/06
 Problem Source: https://www.acmicpc.net/problem/19238
 Version: Python 3.10.4
"""

import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

sx, sy = map(int, input().split())
sx -= 1; sy -= 1
guests = {}
for i in range(1, m+1):
    a,b,c,d = map(int, input().split())
    guests[i] = (a-1, b-1, c-1, d-1)
    graph[a-1][b-1] = -i

move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def transfer(x, y, gx, gy):
    if x == gx and y == gy: return 0
    visited = [[False] * n for _ in range(n)]
    dis = [[0] * n for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + move[i][0]; ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] != True:
                visited[nx][ny] = True
                queue.append((nx, ny))
                dis[nx][ny] = dis[x][y] + 1
                if nx == gx and ny == gy: return dis[gx][gy]
    return -1

def check(x, y):
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    hq = [(0, x, y)]

    while hq:
        dis, x, y = heappop(hq)

        if graph[x][y] < 0: return -graph[x][y], dis
        for i in range(4):
            nx = x + move[i][0]; ny = y + move[i][1]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] != True:
                visited[nx][ny] = True
                heappush(hq, (dis + 1, nx, ny))
    return -1, -1

while m:
    min_idx, min_dis = check(sx, sy)
    fuel -= min_dis

    if fuel <= 0 or min_dis == -1: fuel = -1; break
    dis = transfer(guests[min_idx][0], guests[min_idx][1], guests[min_idx][2], guests[min_idx][3])
    fuel -= dis

    if fuel < 0 or dis == -1: fuel = -1; break
    sx = guests[min_idx][2]; sy = guests[min_idx][3]
    graph[guests[min_idx][0]][guests[min_idx][1]] = 0
    del guests[min_idx]
    fuel += 2 * dis
    m -= 1

print(fuel)