"""
 백준 8393번: 합 풀이
 Author: CodeAlphas
 Date: 2022/04/15
 Problem Source: https://www.acmicpc.net/problem/8393
 Version: Python 3.10.4
"""

n = int(input())
result = 0

for i in range(1, n+1):
    result += i

print(result)