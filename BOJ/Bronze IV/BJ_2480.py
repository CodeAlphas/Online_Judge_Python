"""
 백준 2480번: 주사위 세개 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/2480
 Version: Python 3.10.4
"""

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + 1000 * a)
elif a == b or b == c:
    print(1000 + 100 * b)
elif a == c:
    print(1000 + 100 * a)
else:
    print(100 * max(a, b, c))