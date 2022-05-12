"""
 백준 2439번: 별 찍기 - 2 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/2439
 Version: Python 3.10.4
"""

n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)