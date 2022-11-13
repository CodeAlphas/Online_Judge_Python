"""
 프로그래머스: 3진법 뒤집기 풀이
 Author: CodeAlphas
 Date: 2022/11/13
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/68935
 Version: Python 3.10.4
"""

def translate(n):
    result = ""
    while n != 0:
        result += str(n % 3)
        n = n // 3
    return int(result, 3)
    
def solution(n):
    return translate(n)