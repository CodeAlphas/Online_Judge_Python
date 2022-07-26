"""
 백준 15654번: N과 M (5) 풀이
 Author: CodeAlphas
 Date: 2022/07/06
 Problem Source: https://www.acmicpc.net/problem/15654
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

def solution(result, depth):
    if depth == m:
        print(*result)
        return
    else:
        for num in array:
            if num not in result:
                solution(result + [num], depth+1)
            
solution([], 0)