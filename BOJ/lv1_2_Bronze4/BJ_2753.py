"""
 백준 2753번: 윤년 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2753
 Version: Python 3.10.4
"""

year = int(input())

if (year % 4) == 0 and (year % 100 != 0) or (year % 400) == 0:
    print(1)
else:
    print(0)