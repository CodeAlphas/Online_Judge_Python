"""
 백준 9375번: 패션왕 신해빈 풀이
 Author: CodeAlphas
 Date: 2022/06/13
 Problem Source: https://www.acmicpc.net/problem/9375
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

for test_case in range(t):
    n = int(input())
    result = 1

    clothes = {}
    for i in range(n):
        cloth, c_type = input().split()
        if c_type in clothes:
            clothes[c_type] += 1
        else:
            clothes[c_type] = 2

    for c in clothes:
        result = result * clothes[c]

    print(result-1)