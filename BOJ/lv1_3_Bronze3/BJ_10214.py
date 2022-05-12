"""
 백준 10214번: Baseball 풀이
 Author: CodeAlphas
 Date: 2022/04/23
 Problem Source: https://www.acmicpc.net/problem/10214
 Version: Python 3.10.4
"""

t = int(input())

for _ in range(1, t+1):
    x_, y_ = 0, 0
    for _ in range(9):
        x, y = map(int, input().split())
        x_ += x; y_ += y

    if x_ > y_:
        print("Yonsei")
    elif x_ < y_:
        print("Korea")
    else:
        print("Draw")