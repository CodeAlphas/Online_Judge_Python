"""
 프로그래머스: 콜라 문제 풀이
 Author: CodeAlphas
 Date: 2022/11/07
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/132267
 Version: Python 3.10.4
"""

def solution(a, b, n):
    answer = 0
    while n > a - 1:
        temp = (n // a) * b
        answer += temp
        n = temp + n % a

    return answer