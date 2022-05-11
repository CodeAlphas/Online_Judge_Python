"""
 백준 2588번: 곱셈 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2588
 Version: Python 3.10.4
"""

a = int(input())
b = input()

i = len(b) - 1
while i >= 0:
    print(a * int(b[i]))
    i -= 1

print(a * int(b))