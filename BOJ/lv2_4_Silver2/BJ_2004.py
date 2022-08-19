"""
 백준 2004번: 조합 0의 개수 풀이
 Author: CodeAlphas
 Date: 2022/08/19
 Problem Source: https://www.acmicpc.net/problem/2004
 Version: Python 3.10.4
"""

n, m = map(int, input().split())

def count_number(origin, num):
    count = 0
    while origin:
        origin //= num
        count += origin
    return count

print(min(count_number(n, 2)-count_number(m, 2)-count_number(n-m, 2), \
    count_number(n, 5)-count_number(m, 5)-count_number(n-m, 5)))
