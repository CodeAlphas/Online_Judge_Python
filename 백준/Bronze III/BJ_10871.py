"""
 백준 10871번: X보다 작은 수 풀이
 Author: CodeAlphas
 Date: 2022/04/28
 Problem Source: https://www.acmicpc.net/problem/10871
 Version: Python 3.10.4
"""

n, x = map(int, input().split())
a = list(map(int, input().split()))
a_len = len(a)

for i in range(a_len):
    if a[i] < x:
        print(a[i], end = " ")