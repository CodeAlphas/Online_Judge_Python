"""
 백준 3009번: 네 번째 점 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/3009
 Version: Python 3.10.4
"""

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x); y_list.append(y)

for x in x_list:
    if x_list.count(x) == 1:
        r_x = x

for y in y_list:
    if y_list.count(y) == 1:
        r_y = y

print(r_x, r_y) # 네 번째 점의 좌표
    

