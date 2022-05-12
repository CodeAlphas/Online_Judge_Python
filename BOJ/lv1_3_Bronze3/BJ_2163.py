"""
 백준 2163번: 초콜릿 자르기 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/2163
 Version: Python 3.10.4
"""

n, m = map(int, input().split())
print((n-1) + (n)*(m-1))