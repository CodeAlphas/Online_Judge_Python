"""
 백준 10872번: 팩토리얼 풀이
 Author: CodeAlphas
 Date: 2022/04/28
 Problem Source: https://www.acmicpc.net/problem/10872
 Version: Python 3.10.4
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))