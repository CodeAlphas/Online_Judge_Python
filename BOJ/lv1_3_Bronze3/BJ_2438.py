"""
 백준 2438번: 별 찍기 - 1 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/2438
 Version: Python 3.10.4
"""

n = int(input())

for i in range(1, n+1):
    print("*" * i)