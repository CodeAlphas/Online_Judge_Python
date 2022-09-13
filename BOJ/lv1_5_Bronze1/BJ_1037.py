"""
 백준 1037번: 약수 풀이
 Author: CodeAlphas
 Date: 2022/09/13
 Problem Source: https://www.acmicpc.net/problem/1037
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
divisors = list(map(int, input().split()))
divisors.sort()

if n == 1:
    print(divisors[0]**2)
else:
    print(divisors[0]*divisors[n-1])