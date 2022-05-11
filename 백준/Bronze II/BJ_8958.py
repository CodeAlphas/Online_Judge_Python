"""
 백준 8958번: OX퀴즈 풀이
 Author: CodeAlphas
 Date: 2022/04/17
 Problem Source: https://www.acmicpc.net/problem/8958
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

tc = int(input())
array = []
jumsu = 0
result = 0

for i in range(tc):
    array = list(input().rstrip())
    for j in array:
        if j == 'O':
            jumsu += 1
        if j == 'X':
            jumsu = 0
        result += jumsu
    jumsu = 0
    print(result)
    result = 0

