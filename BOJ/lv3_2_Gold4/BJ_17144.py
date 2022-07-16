"""
 백준 17144번: 미세먼지 안녕! 풀이
 Author: CodeAlphas
 Date: 2022/06/25
 Problem Source: https://www.acmicpc.net/problem/17144
 Version: Python 3.10.4
"""

# PyPy3만 통과
# import sys
# from collections import deque
# input = sys.stdin.readline

# r, c, t = map(int, input().split())
# maps = []; cleaner = []
# for i in range(r):
#     temp = list(map(int, input().split()))
#     if temp[0] == -1:
#         cleaner.append((i, 0))
#     maps.append(temp)

# def spread_dust(maps):
#     move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     x1, y1 = cleaner[0]; x2, y2 = cleaner[1]; dust_list = []

#     for x in range(r):
#         for y in range(c):
#             if maps[x][y] != 0 and maps[x][y] != -1:
#                 dust_list.append((x, y, maps[x][y]))

#     for x, y, d in dust_list:
#         count = 0
#         for i in range(4):
#             nx = x + move[i][0]; ny = y + move[i][1]
#             if 0 <= nx < r and 0 <= ny < c and (nx != x1 or ny != y1) and (nx != x2 or ny != y2):
#                 maps[nx][ny] += d // 5
#                 count += 1
#         maps[x][y] -= (d // 5) * count
#     return maps

# def move_dust(maps):
#     move1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
#     move2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     x1, y1 = cleaner[0]; x2, y2 = cleaner[1]

#     n = 0; queue = deque([(x1, y1+1, maps[x1][y1+1])])
#     maps[x1][y1+1] = 0
#     while queue:
#         x, y, d = queue.popleft()
#         nx = x + move1[n][0]; ny = y + move1[n][1]
#         if 0 <= nx < r and 0 <= ny < c:        
#             if nx == x1 and ny == y1: break
#             queue.append((nx, ny, maps[nx][ny]))
#             maps[nx][ny] = d
#         else:
#             n += 1
#             queue.append((x, y, d))

#     n = 0; queue = deque([(x2, y2+1, maps[x2][y2+1])])
#     maps[x2][y2+1] = 0
#     while queue:
#         x, y, d = queue.popleft()
#         nx = x + move2[n][0]; ny = y + move2[n][1]
#         if 0 <= nx < r and 0 <= ny < c:
#             if nx == x2 and ny == y2: break
#             queue.append((nx, ny, maps[nx][ny]))
#             maps[nx][ny] = d
#         else:
#             n += 1
#             queue.append((x, y, d))

#     return maps

# while t >= 1:
#     maps = spread_dust(maps)
#     maps = move_dust(maps)
#     t-= 1

# result = 0
# for x in range(r):
#     for y in range(c):
#         if maps[x][y] != -1 and maps[x][y] != 0:
#             result += maps[x][y]

# print(result)

# 2 Python3 통과
import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
maps = []; cleaner = []
for i in range(r):
    temp = list(map(int, input().split()))
    if temp[0] == -1:
        cleaner.append((i, 0))
    maps.append(temp)

def spread_dust(maps):
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    temp = [[0] * c for _ in range(r)]
    x1, y1 = cleaner[0]; x2, y2 = cleaner[1]

    for x in range(r):
        for y in range(c):
            if maps[x][y] == -1 or maps[x][y] == 0:
                continue

            count = 0; d = maps[x][y] // 5
            for i in range(4):
                nx = x + move[i][0]; ny = y + move[i][1]
                if 0 <= nx < r and 0 <= ny < c and (nx != x1 or ny != y1) and (nx != x2 or ny != y2):
                    temp[nx][ny] += d
                    count += 1
            temp[x][y] += maps[x][y] - d * count
    return temp

def move_dust(maps):
    move1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    move2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x1, y1 = cleaner[0]; x2, y2 = cleaner[1]
    
    n = 0; d = maps[x1][y1+1]
    maps[x1][y1+1] = 0; x = x1; y = y1+1
    while True:
        nx = x + move1[n][0]; ny = y + move1[n][1]
        if 0 <= nx < r and 0 <= ny < c:        
            if nx == x1 and ny == y1: break
            x = nx; y = ny; temp = maps[nx][ny]
            maps[nx][ny] = d
            d = temp
        else:
            n += 1

    n = 0; d = maps[x2][y2+1]
    maps[x2][y2+1] = 0; x = x2; y = y2+1
    while True:
        nx = x + move2[n][0]; ny = y + move2[n][1]
        if 0 <= nx < r and 0 <= ny < c:        
            if nx == x2 and ny == y2: break
            x = nx; y = ny; temp = maps[nx][ny]
            maps[nx][ny] = d
            d = temp
        else:
            n += 1

    return maps

while t >= 1:
    maps = spread_dust(maps)
    maps = move_dust(maps)
    t-= 1

result = 0
for x in range(r):
    for y in range(c):
        result += maps[x][y]

print(result)