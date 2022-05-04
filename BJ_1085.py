"""
 1085번: 직사각형에서 탈출
 Problem Source: https://www.acmicpc.net/problem/1085
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/15.
"""

x, y, w, h = map(int, input().split())

a, b, c, d = x, y, h-y, w-x
print(min(a, b, c, d))