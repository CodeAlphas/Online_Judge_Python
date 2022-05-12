"""
 백준 11653번: 소인수분해 풀이
 Author: CodeAlphas
 Date: 2022/04/27
 Problem Source: https://www.acmicpc.net/problem/11653
 Version: Python 3.10.4
"""

n = int(input())

def solution(n):
    if n == 1:
        return
    else:
        while n > 1:
            for i in range(2, n+1):
                if n % i == 0:
                    print(i)
                    n //= i
                    break

solution(n)

    

