"""
 백준 21608번: 상어 초등학교 풀이
 Author: CodeAlphas
 Date: 2022/10/10
 Problem Source: https://www.acmicpc.net/problem/21608
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
n = int(input())

seat = {}
for _ in range(n**2):
    num, a, b, c, d = map(int, input().split())
    seat[num] = [a, b, c, d]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def check_student(num, x, y):
    count = 0
    for i in range(4):
        nx = x + direction[i][0]; ny = y + direction[i][1]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0 and graph[nx][ny] in seat[num]:
            count += 1
    return count

def check_vacant(x, y):
    count = 0
    for i in range(4):
        nx = x + direction[i][0]; ny = y + direction[i][1]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            count += 1
    return count

def decide(num):
    global graph, visited

    counts_student = {4: [], 3: [], 2: [], 1: [], 0: []}
    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                count = check_student(num, x, y)
                counts_student[count].append([x, y])

    counts_vacant = {4: [], 3: [], 2: [], 1: [], 0: []}
    for num in counts_student:
        if len(counts_student[num]) != 0:
            while len(counts_student[num]) != 0:
                x, y = counts_student[num].pop()
                count = check_vacant(x, y)
                counts_vacant[count].append([x, y])
            break

    for num in counts_vacant:
        if len(counts_vacant[num]) != 0:
            return counts_vacant[num][-1]

def calculate(count):
    if count == 0: return 0
    elif count == 1: return 1
    elif count == 2: return 10
    elif count == 3: return 100
    else: return 1000

graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for num in seat:
    x, y = decide(num)
    visited[x][y] = True
    graph[x][y] = num

result = 0
for x in range(n):
    for y in range(n):
        count = check_student(graph[x][y], x, y)
        result += calculate(count)

print(result)