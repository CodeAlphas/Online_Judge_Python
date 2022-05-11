"""
 백준 1003번: 피보나치 함수 풀이
 Author: CodeAlphas
 Date: 2022/04/15
 Problem Source: https://www.acmicpc.net/problem/1003
 Version: Python 3.10.4
"""

fibo = [(1, 0), (0, 1)]

for i in range(2, 41):
    count_zero = fibo[i-1][0] + fibo[i-2][0]
    count_one = fibo[i-1][1] + fibo[i-2][1]
    fibo.append((count_zero, count_one)) 

t = int(input()) # 테스트 케이스 

for test_case in range(1, t+1): 

    n = int(input())
    z_s, o_s = fibo[n]
    print(z_s, o_s)

