"""
 백준 10026번: 적록색약 풀이
 Author: CodeAlphas
 Date: 2022/05/26
 Problem Source: https://www.acmicpc.net/problem/10026
 Version: Python 3.10.4
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
drawing = []

for _ in range(n):
    drawing.append(list(input().strip()))

drawing2 = [[-1 for _ in range(n)] for _ in range(n)] 

for x in range(n):
    for y in range(n):
        if drawing[x][y] == "R":
            drawing2[x][y] = "G"
        else:
            drawing2[x][y] = drawing[x][y]

def dfs(x, y, color, mode):

    if x < 0 or x >= n or y < 0 or y >= n:
        return 

    if mode == 1:
        if drawing[x][y] == color:
            drawing[x][y] = "v"

            dfs(x, y-1, color, 1)
            dfs(x, y+1, color, 1)
            dfs(x-1, y, color, 1)
            dfs(x+1, y, color, 1)
            return 
    else:
        if drawing2[x][y] == color:
            drawing2[x][y] = "v"

            dfs(x, y-1, color, 2)
            dfs(x, y+1, color, 2)
            dfs(x-1, y, color, 2)
            dfs(x+1, y, color, 2)
            return       

    return 

result = 0
for x in range(n):
    for y in range(n):
        if drawing[x][y] != "v":
            dfs(x, y, drawing[x][y], 1)
            result += 1

result2 = 0
for x in range(n):
    for y in range(n):
        if drawing2[x][y] != "v":
            dfs(x, y, drawing2[x][y], 2)
            result2 += 1

print(result, result2)