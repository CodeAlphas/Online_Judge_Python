"""
 백준 16235번: 나무 재테크 풀이
 Author: CodeAlphas
 Date: 2022/07/01
 Problem Source: https://www.acmicpc.net/problem/16235
 Version: Python 3.10.4
"""

# PyPy3만 통과
import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split()) # 배열 크기, 나무의 갯수, k년 후
maps = [[5] * n for _ in range(n)] # 양분 배열
a = [list(map(int, input().split())) for _ in range(n)] # 각 칸에 추가되는 양분의 양

trees = [[deque() for _ in range(n)] for _ in range(n)] # 나무 배열
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

def spring_summer(trees):
    global maps

    for x in range(n):
        for y in range(n):
            num = len(trees[x][y])
            for z in range(num):
                if maps[x][y] >= trees[x][y][z]:
                    maps[x][y] -= trees[x][y][z]
                    trees[x][y][z] += 1
                else:
                    for _ in range(z, num):
                        maps[x][y] += trees[x][y].pop()//2
                    break

    return trees

def fall_winter(trees):
    global maps
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for x in range(n):
        for y in range(n):
            num = len(trees[x][y])
            for z in range(num):
                if trees[x][y][z] % 5 == 0:
                    for i in range(8):
                        nx = x + dir[i][0]; ny = y + dir[i][1]
                        if 0 <= nx < n and 0 <= ny < n:
                            trees[nx][ny].appendleft(1)
            maps[x][y] += a[x][y]

    return trees

while k:
    trees = spring_summer(trees)
    trees = fall_winter(trees)
    k -= 1

result = 0
for x in range(n):
    for y in range(n):
        result += len(trees[x][y])

print(result)
