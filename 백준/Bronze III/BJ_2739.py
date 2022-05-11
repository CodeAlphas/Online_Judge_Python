"""
 백준 2739번: 구구단 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2739
 Version: Python 3.10.4
"""

n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" %(n, i, n * i))
