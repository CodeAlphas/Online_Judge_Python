"""
 백준 18111번: 마인크래프트 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/18111
 Version: Python 3.10.4
"""

# PyPy3만 통과
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split()) # 세로, 가로, 처음 가지고 있는 블록 개수

maps_heights = []
for _ in range(n):
    maps_heights += list(map(int, input().split()))

maps_heights.sort(reverse=True)
max_num = maps_heights[0]
min_num = maps_heights[-1]
min_time = int(1e10)
heights = []

for height in range(min_num, max_num + 1):
    time = 0 # 작업에 걸리는 시간
    blocks = b # 가지고 있는 블록
    flag = False

    for i in maps_heights:
        if height < i:
            a = 2 * (i-height)
            time += a
            blocks += a//2
        elif height > i:
            c = height - i
            if c <= blocks:
                time += c
                blocks -= c
            else:
                flag = True
                break

    if time <= min_time and not flag:
        min_time = min(time, min_time)
        heights.append(height)

print(min_time, heights[-1])

