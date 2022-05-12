"""
 백준 11050번: 이항 계수 1 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/11050
 Version: Python 3.10.4
"""

# 1
# def factorial(num):
#     if num == 0:
#         return 1
#     elif num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)

# n, k = map(int, input().split())

# print(factorial(n)//(factorial(n-k) * factorial(k)))

# 2
from math import comb

n, k = map(int, input().split())
print(comb(n, k))





