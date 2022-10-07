"""
 백준 20056번: 마법사 상어와 파이어볼 풀이
 Author: CodeAlphas
 Date: 2022/10/07
 Problem Source: https://www.acmicpc.net/problem/20056
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fb_info = {}
graphs = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    fb_info[i] = [ri-1, ci-1, mi, si, di]
    graphs[ri-1][ci-1].append(i)
max_id = m

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def move_fireballs():
    global graphs, fb_info
    for i in fb_info:
        x, y, m, s, d = fb_info[i]
        nx = (x + dirs[d][0] * s) % n; ny = (y + dirs[d][1] * s) % n
        graphs[x][y].remove(i)
        graphs[nx][ny].append(i)
        fb_info[i] = [nx, ny, m, s, d]

def sum_div_del_fireballs(x, y):
    global graphs, fb_info, max_id
    sum_m = 0; sum_s = 0; ch = fb_info[graphs[x][y][0]][4] % 2; num = 0; ids = []
    check = True
    for id in graphs[x][y]:
        sum_m += fb_info[id][2]
        sum_s += fb_info[id][3]
        t_ch = fb_info[id][4] % 2
        if t_ch != ch: check = False
        ids.append(id)
        del fb_info[id]
        num += 1

    for id in ids: graphs[x][y].remove(id)

    if sum_m//5 != 0:
        if check:
            for i in range(0, 7, 2):
                max_id += 1
                graphs[x][y].append(max_id)
                fb_info[max_id] = [x, y, sum_m//5, sum_s//num, i]
        else:
            for i in range(1, 8, 2):
                max_id += 1
                graphs[x][y].append(max_id)
                fb_info[max_id] = [x, y, sum_m//5, sum_s//num, i]

def check():
    for x in range(n):
        for y in range(n):
            if len(graphs[x][y]) >= 2:
                sum_div_del_fireballs(x, y)

while k:
    move_fireballs()
    check()
    k -= 1

result = 0
for id in fb_info:
    result += fb_info[id][2]
print(result)