"""
 백준 7568번: 덩치 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/7568
 Version: Python 3.10.4
"""

n = int(input())
humans = []

for _ in range(n):
    x, y = map(int, input().split())
    humans.append((x, y))

humans_rank = [] # 덩치 순위
for x, y in humans:
    temp = [co for co in humans]
    temp.remove((x, y))
    count = 1
    for x1, y1 in temp:
        if x < x1 and y < y1:
            count += 1
    humans_rank.append(count)
        
for i in humans_rank:
    print(i, end = ' ')