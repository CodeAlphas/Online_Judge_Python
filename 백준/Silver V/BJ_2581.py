"""
 백준 2581번: 소수 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2581
 Version: Python 3.10.4
"""

def check_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5)+1):
            if x % i == 0:
                return False
        return True

m = int(input()); n = int(input())
sum_number = 0
flag = True

for i in range(m, n+1):
    if check_prime_number(i):
        sum_number += i
        if flag:
            min_number = i
            flag = False

if flag:
    print(-1)
else:
    print(sum_number)
    print(min_number)