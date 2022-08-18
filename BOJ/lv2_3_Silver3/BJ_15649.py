"""
 백준 15649번: N과 M (1) 풀이
 Author: CodeAlphas
 Date: 2022/08/18
 Problem Source: https://www.acmicpc.net/problem/15649
 Version: Python 3.10.4
"""

n, m = map(int, input().split())

def solution(depth, seq, n, m):
    if depth == m:
        print(*seq)
    else:
        for i in range(1, n+1):
            if i not in seq:
                solution(depth+1, seq + [i], n, m)

solution(0, [], n, m)