"""
 백준 3052번: 나머지 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/3052
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
array = []
result = []

for i in range(10):
    array.append(int(input())%42)

for i in array:
    if i not in result:
        result.append(i)

print(len(result))