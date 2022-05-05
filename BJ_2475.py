"""
 2475번: 검증수
 Problem Source: https://www.acmicpc.net/problem/2475
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/04.
"""

a, b, c, d, e = map(int, input().split())

print((a**2+b**2+c**2+d**2+e**2)%10)