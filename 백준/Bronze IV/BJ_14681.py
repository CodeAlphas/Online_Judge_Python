"""
 백준 14681번: 사분면 고르기 풀이
 Author: CodeAlphas
 Date: 2022/04/16
 Problem Source: https://www.acmicpc.net/problem/14681
 Version: Python 3.10.4
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    elif y < 0:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    elif y < 0:
        print(3)    