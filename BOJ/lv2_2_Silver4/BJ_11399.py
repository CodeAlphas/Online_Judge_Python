"""
 백준 11399번: ATM 풀이
 Author: CodeAlphas
 Date: 2022/06/06
 Problem Source: https://www.acmicpc.net/problem/11399
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0; temp = 0

for time in p:
    temp += time
    result += temp

print(result)