"""
 백준 2839번: 설탕 배달 풀이
 Author: CodeAlphas
 Date: 2022/05/02
 Problem Source: https://www.acmicpc.net/problem/2839
 Version: Python 3.10.4
"""

n = int(input()) # 상근이가 배달해야 하는 설탕의 킬로그램
result = 0 # 봉지 개수

while n > 0:
    if n % 5 == 0:
        n -= 5
        result += 1
    else:
        n -= 3
        result += 1

if n == 0:
    print(result)
else:
    print(-1)
