"""
 프로그래머스: 피보나치 수 풀이
 Author: CodeAlphas
 Date: 2022/09/24
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12945
 Version: Python 3.10.4
"""

def solution(n):

    f = [0] * (n+1)
    f[0] = 0; f[1] = 1
    for i in range(2, n+1):
        f[i] = (f[i-1] + f[i-2]) % 1234567
    
    return f[n]