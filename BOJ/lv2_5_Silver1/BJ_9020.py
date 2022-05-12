"""
 백준 9020번: 골드바흐의 추측 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/9020
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수
num = 10000
prime_number_list = [True for _ in range(num+1)]

for i in range(2, int(num**0.5) + 1):
    if prime_number_list[i] == True:
        j = 2
        while i*j <= num:
            prime_number_list[i*j] = False
            j += 1

for test_case in range(t):
    n = int(input()) # 주어진 수 n
    middle = n//2

    for i in range(middle, n-1):
        if prime_number_list[i] and prime_number_list[n-i]:
            print(n-i, i)
            break

