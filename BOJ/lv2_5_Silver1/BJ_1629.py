"""
 백준 1629번: 곱셈 풀이
 Author: CodeAlphas
 Date: 2022/06/18
 Problem Source: https://www.acmicpc.net/problem/1629
 Version: Python 3.10.4
"""

a, b, c = map(int, input().split())

def pow(a1, b1, c1):
    if b1 == 1: return a1 % c1
    elif b1 % 2 == 0:
        return (pow(a1, b1//2, c1) ** 2) % c1
    else:
        return ((pow(a1, b1//2, c1) ** 2) * (a1 % c1)) % c1

print(pow(a, b, c))
