"""
 백준 21611번: 마법사 상어와 블리자드 풀이
 Author: CodeAlphas
 Date: 2022/10/12
 Problem Source: https://www.acmicpc.net/problem/21611
 Version: Python 3.10.4
"""

# PyPy3 통과
import sys
input = sys.stdin.readline

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def cal_graph_num():
    global graph_num
    visited = [[False] * n for _ in range(n)]
    x = n // 2; y = n // 2
    visited[x][y] = True
    dir = 0; num = 1
    while x != 0 or y != 0:
        nx = x + direction[dir][0]; ny = y + direction[dir][1]
        if visited[nx][ny] == False:
            graph_num[nx][ny] = num
            visited[nx][ny] = True
        else:
            if dir == 0: dir = 3
            else: dir -= 1
            nx = x + direction[dir][0]; ny = y + direction[dir][1]
            graph_num[nx][ny] = num
            visited[nx][ny] = True
        x = nx; y = ny
        num += 1
        dir += 1; dir %= 4

def calculate(num, c):
    global result
    result += num * c

b_direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
def blizzard(d, s):
    global balls
    x = n // 2; y = n // 2
    for _ in range(s):
        nx = x + b_direction[d][0]; ny = y + b_direction[d][1]
        balls[graph_num[nx][ny]] = 0
        x = nx; y = ny

def move():
    global balls
    len_balls = len(balls)
    for i in range(1, len_balls):
        if balls[i] == 0:
            for j in range(i+1, len_balls):
                if balls[j] != 0:
                    balls[i], balls[j] = balls[j], balls[i]
                    break

def explosion():
    global balls
    len_balls = len(balls)
    while True:
        ball_count = 0
        count = 1; num = balls[1]; s_index = 1
        for i in range(2, len_balls):
            if balls[i] == num:
                count += 1
            else:
                if count >= 4:
                    ball_count += 1
                    balls[s_index:i] = [0] * (i - s_index)
                    calculate(num, count)
                count = 1
                num = balls[i]
                s_index = i
        move()
        if ball_count == 0: break

def divide():
    global balls
    len_balls = len(balls)
    t_balls = [0] * (n ** 2)
    count = 1; num = balls[1]; t_index = 1
    for i in range(2, len_balls):
        if balls[i] == num:
            count += 1
        else:
            t_balls[t_index: t_index + 2] = [count, num]
            t_index += 2
            count = 1
            num = balls[i]

    balls = t_balls[:n**2]

n, m = map(int, input().split())
graph_num = [[0] * n for _ in range(n)]
cal_graph_num()

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

balls = [0] * (n ** 2)
for x in range(n):
    for y in range(n):
        balls[graph_num[x][y]] = graph[x][y]

orders = []
for _ in range(m):
    orders.append(list(map(int, input().split())))

result = 0
for d, s in orders:
    blizzard(d, s)
    move()
    explosion()
    divide()

print(result)