"""
 백준 15651번: N과 M (3) 풀이
 Author: CodeAlphas
 Date: 2022/09/12
 Problem Source: https://www.acmicpc.net/problem/15651
 Version: Python 3.10.4
"""

n, m = map(int, input().split())
array = list(i for i in range(1, n+1))

def check(array, temp):
    if len(temp) == m:
        print(*temp)
        return

    for num in array:
        check(array, temp + [num])

check(array, [])