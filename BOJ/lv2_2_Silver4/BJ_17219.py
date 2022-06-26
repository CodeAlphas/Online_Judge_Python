"""
 백준 17219번: 비밀번호 찾기 풀이
 Author: CodeAlphas
 Date: 2022/06/11
 Problem Source: https://www.acmicpc.net/problem/17219
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sites = {}
for _ in range(n):
    site, password = input().split()
    sites[site] = password

for _ in range(m):
    print(sites[input().rstrip()])



