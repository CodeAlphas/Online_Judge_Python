"""
 백준 17779번: 게리맨더링 2 풀이
 Author: CodeAlphas
 Date: 2022/07/18
 Problem Source: https://www.acmicpc.net/problem/17779
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
maps = []; total = 0
for _ in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)
    total += sum(temp)

def check(x, y, d1, d2):
    one, two, three, four = 0, 0, 0, 0
    t_y = y + 1
    for i in range(x+d1):
        if i >= x:
            t_y -= 1
        one += sum(maps[i][:t_y])
    
    t_y = y + 1
    for j in range(x+d2+1):
        if j > x:
            t_y += 1
        two += sum(maps[j][t_y:])

    t_y = y - d1
    for k in range(x+d1, n):
        three += sum(maps[k][:t_y])
        if k < x + d1 + d2:
            t_y += 1
    
    t_y = y + d2 - n
    for l in range(x+d2+1, n):
        four += sum(maps[l][t_y:])
        if l <= x + d1 + d2:
            t_y -= 1

    five = total - (one + two + three + four)
    return max(one, two, three, four, five) - min(one, two, three, four, five)

result = int(1e10)
for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x+d1+d2 <= n and 1 <= y-d1 < y < y+d2 <= n:
                    result = min(result, check(x, y, d1, d2))

print(result)