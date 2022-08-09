"""
 백준 17837번: 새로운 게임 2 풀이
 Author: CodeAlphas
 Date: 2022/07/20
 Problem Source: https://www.acmicpc.net/problem/17837
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
colors = []
for _ in range(n):
    colors.append(list(map(int, input().split())))

pieces = {}; maps = [[[] for _ in range(n)] for _ in range(n)]
for i in range(1, k+1):
    x, y, dir = map(int, input().split())
    pieces[i] = (x-1, y-1, dir)
    maps[x-1][y-1].append(i)

direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

def change_dir(dir):
    if dir == 1: n_dir = 2
    elif dir == 2: n_dir = 1
    elif dir == 3: n_dir = 4
    elif dir == 4: n_dir = 3
    return n_dir

def move(x, y, dir, i, count):
    global maps, pieces

    nx = x + direction[dir][0]; ny = y + direction[dir][1]

    if 0 <= nx < n and 0 <= ny < n:
        if colors[nx][ny] == 0:
            a = maps[x][y].index(i)
            maps[nx][ny] += maps[x][y][a:]
            maps[x][y] = maps[x][y][:a]
            for index in maps[nx][ny]:
                _dir = pieces[index][2]
                pieces[index] = (nx, ny, _dir)
        elif colors[nx][ny] == 1:
            a = maps[x][y].index(i)
            temp = maps[x][y][a:]
            temp.reverse()
            maps[nx][ny] += temp
            maps[x][y] = maps[x][y][:a]
            for index in maps[nx][ny]:
                _dir = pieces[index][2]
                pieces[index] = (nx, ny, _dir)
        else:
            if count == 0:
                n_dir = change_dir(dir)
                pieces[i] = (x, y, n_dir)
                nx, ny = move(x, y, n_dir, i, count+1)
            else:
                return x, y
    else:
        if count == 0:
            n_dir = change_dir(dir)
            pieces[i] = (x, y, n_dir)
            nx, ny = move(x, y, n_dir, i, count+1)
        else: 
            return x, y

    return nx, ny

turn = 0; ch = False
while True:

    turn += 1

    for i in range(1, k+1):
        x, y, dir = pieces[i]
        nx, ny = move(x, y, dir, i, 0)
        if len(maps[nx][ny]) >= 4:
            ch = True
            break

    if turn > 1000:
        turn = -1
        break
    if ch:
        break

print(turn)