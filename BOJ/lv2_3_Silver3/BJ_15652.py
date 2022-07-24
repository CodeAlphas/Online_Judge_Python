"""
 백준 15652번: N과 M (4) 풀이
 Author: CodeAlphas
 Date: 2022/07/03
 Problem Source: https://www.acmicpc.net/problem/15652
 Version: Python 3.10.4
"""

n, m = map(int, input().split())

def solution(array, depth):
    if depth == m:
        array.pop(0)
        print(*array)
        return
    
    for i in range(1, n+1):
        if array[-1] <= i:
            solution(array + [i], depth + 1)

solution([0], 0)