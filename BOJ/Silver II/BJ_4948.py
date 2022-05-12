"""
 백준 4948번: 베르트랑 공준 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/4948
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

max_num = 123456 * 2
array = [True for _ in range(max_num + 1)]
array[1] = False

for i in range(2, int(max_num ** 0.5) + 1):
    j = 2
    while i*j <= max_num:
        array[i*j] = False
        j += 1

while(True):
    n = int(input())
    if n == 0:
        break
    else:
        result = 0
        m = 2 * n

        for i in range(n + 1, m + 1):
            if array[i] == True:
                result += 1

        print(result)