"""
 백준 10430번: 나머지 풀이
 Author: CodeAlphas
 Date: 2022/04/23
 Problem Source: https://www.acmicpc.net/problem/10430
 Version: Python 3.10.4
"""

a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)