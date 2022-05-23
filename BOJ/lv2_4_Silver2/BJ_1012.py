"""
 백준 1012번: 유기농 배추 풀이
 Author: CodeAlphas
 Date: 2022/05/21
 Problem Source: https://www.acmicpc.net/problem/1012
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(x, y):

    if x < 0 or x >= n or y < 0 or y >= m:
        return
    
    if maps[x][y] == 1:
        maps[x][y] = 0
        for i in range(4):
            solution(x+dx[i], y+dy[i])
        return True

    return False

for test_case in range(t):
    m, n, k = map(int, input().split())
    maps = [[0 for  _ in range(m)] for _ in range(n)]
    insects = []
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1
            
    for i in range(n):
        for j in range(m):
            if solution(i, j):
                result += 1

    print(result)