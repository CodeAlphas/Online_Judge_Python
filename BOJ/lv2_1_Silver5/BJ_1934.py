"""
 백준 1934번: 최소공배수 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/1934
 Version: Python 3.10.4
"""

t = int(input())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a,b))

