"""
 백준 17143번: 낚시왕 풀이
 Author: CodeAlphas
 Date: 2022/07/13
 Problem Source: https://www.acmicpc.net/problem/17143
 Version: Python 3.10.4
"""

# PyPy3만 통과
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
sharks = [[0] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split()) # 위치, 속력, 이동 방향, 크기
    sharks[r-1][c-1] = [s, d, z]

def catch(sharks, j):
    global result

    for i in range(R):
        if sharks[i][j]:
            result += sharks[i][j][2]
            sharks[i][j] = 0
            break
    return sharks

def direction(x, y, s, d):
    dir = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    nx = x; ny = y

    if d == 1 or d == 2:
        s %= 2*(R-1)
    else:
        s %= 2*(C-1)

    for _ in range(s):
        nx = x + dir[d][0]; ny = y + dir[d][1]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            else: d = 3
            nx = x + dir[d][0]; ny = y + dir[d][1]
        x = nx; y = ny
    return nx, ny, d

def move(sharks):
    temp_sharks = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if sharks[x][y]:
                s, d, z = sharks[x][y]
                nx, ny, nd = direction(x, y, s, d)
                if temp_sharks[nx][ny]:
                    nz = temp_sharks[nx][ny][2]
                    if nz < z:
                        temp_sharks[nx][ny] = [s, nd, z]
                else:
                    temp_sharks[nx][ny] = [s, nd, z]

    sharks = [items[:] for items in temp_sharks]
    return sharks

result = 0
for j in range(C):
    sharks = catch(sharks, j)
    sharks = move(sharks)

print(result)