"""
 백준 3003번: 킹, 퀸, 룩, 비숍, 나이트, 폰 풀이
 Author: CodeAlphas
 Date: 2022/09/06
 Problem Source: https://www.acmicpc.net/problem/3003
 Version: Python 3.10.4
"""

pices = list(map(int, input().split()))
orgin_pices = [1, 1, 2, 2, 2, 8]
result = []
for i in range(6):
    result.append(orgin_pices[i]-pices[i])

print(*result)