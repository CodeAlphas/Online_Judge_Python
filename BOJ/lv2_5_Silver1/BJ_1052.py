"""
 백준 1052번: 물병 풀이
 Author: CodeAlphas
 Date: 2022/09/07
 Problem Source: https://www.acmicpc.net/problem/1052
 Version: Python 3.10.4
"""

n, k = map(int, input().split())
result = 0
bin_n = bin(n)[::-1]

while bin_n.count('1') > k:
    min_idx = bin_n.index('1')
    n += 2**min_idx
    result += 2**min_idx
    bin_n = bin(n)[::-1]

print(result)