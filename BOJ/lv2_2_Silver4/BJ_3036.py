"""
 백준 3036번: 링 풀이
 Author: CodeAlphas
 Date: 2022/08/25
 Problem Source: https://www.acmicpc.net/problem/3036
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
radius_list = list(map(int, input().split()))
radius_first = radius_list[0]
radius_list = radius_list[1:]

def gcd(a, b):
    n = min(a, b)
    while True:
        if a % n == 0 and b % n == 0:
            return n
        else:
            n -= 1
    
for radius in radius_list:
    gcd_num = gcd(radius, radius_first)

    print(f"{int(radius_first/gcd_num)}/{int(radius/gcd_num)}")