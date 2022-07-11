"""
 백준 2407번: 조합 풀이
 Author: CodeAlphas
 Date: 2022/06/21
 Problem Source: https://www.acmicpc.net/problem/2407
 Version: Python 3.10.4
"""

# 1
# import math

# n, m = map(int, input().split())
# print(math.comb(n, m))

# 2
n, m = map(int, input().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n) // (factorial(n-m) * factorial(m)))