"""
 백준 2609번: 최대공약수와 최소공배수 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/2609
 Version: Python 3.10.4
"""

from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))