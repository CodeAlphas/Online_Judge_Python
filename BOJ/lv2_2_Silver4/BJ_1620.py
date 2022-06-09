"""
 백준 1620번: 나는야 포켓몬 마스터 이다솜 풀이
 Author: CodeAlphas
 Date: 2022/06/01
 Problem Source: https://www.acmicpc.net/problem/1620
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon = {} 

for i in range(1, n + 1):
    name = input().rstrip()
    pocketmon[str(i)] = name

reversed_pocketmon = {v:k for k, v in pocketmon.items()}

for _ in range(m):
    question = input().rstrip()
    if question.isalpha():
        print(reversed_pocketmon[question])
    else:
        print(pocketmon[question])
