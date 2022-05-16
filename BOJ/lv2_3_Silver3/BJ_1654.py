"""
 백준 1654번: 랜선 자르기 풀이
 Author: CodeAlphas
 Date: 2022/05/15
 Problem Source: https://www.acmicpc.net/problem/1654
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
for _ in range(k): lan.append(int(input()))
max_lan = max(lan)

def binary_search(start, end):
    results = []

    while start <= end:
        lan_cut = 0
        mid = (start + end) // 2
        for l in lan:
            lan_cut += l//mid

        if lan_cut >= n:
            if mid not in results:
                results.append(mid)
                start = mid + 1
            else:
                break
        else:
            end = mid - 1
    
    return results

print(max(binary_search(1, max_lan)))


