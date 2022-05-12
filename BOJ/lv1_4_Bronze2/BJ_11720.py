"""
 백준 11720번: 숫자의 합 풀이
 Author: CodeAlphas
 Date: 2022/05/02
 Problem Source: https://www.acmicpc.net/problem/11720
 Version: Python 3.10.4
"""

n = int(input())
nn = input()
result = 0

for i in range(n):
    result += int(nn[i])

print(result)