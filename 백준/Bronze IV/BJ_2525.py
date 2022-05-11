"""
 백준 2525번: 오븐 시계 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/2525
 Version: Python 3.10.4
"""

a, b = map(int, input().split())
c = int(input())

i_h = (b + c) // 60 # 증가한 시
i_m = (b + c) - 60 * i_h # 변화한 분

if a + i_h > 23:
    print(a + i_h - 24, i_m)
else:
    print(a + i_h, i_m)