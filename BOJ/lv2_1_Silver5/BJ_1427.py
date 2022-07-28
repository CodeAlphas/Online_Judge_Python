"""
 백준 1427번: 소트인사이드 풀이
 Author: CodeAlphas
 Date: 2022/07/08
 Problem Source: https://www.acmicpc.net/problem/1427
 Version: Python 3.10.4
"""

n = input()
n_len = len(n)
array = []

for i in range(n_len):
    array.append(n[i])

array.sort(reverse = True)
print("".join(array))