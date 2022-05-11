"""
 백준 4153번: 직각삼각형 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/4153
 Version: Python 3.10.4
"""

while(True):
    side = list(map(int, input().split()))
    side.sort()
    a, b, c = side[0], side[1], side[2]

    if (a, b, c) == (0, 0, 0):
        break
    
    if (a ** 2 + b ** 2) == c ** 2:
        print("right")
    else:
        print("wrong")