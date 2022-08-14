"""
 백준 14425번: 문자열 집합 풀이
 Author: CodeAlphas
 Date: 2022/07/25
 Problem Source: https://www.acmicpc.net/problem/14425
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
string_set = {}
for _ in range(n):
    string_set[input().rstrip()]  = 1

result = 0
for _ in range(m):
    if input().rstrip() in string_set:
        result += 1

print(result)