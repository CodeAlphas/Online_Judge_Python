"""
 프로그래머스: 없는 숫자 더하기 풀이
 Author: CodeAlphas
 Date: 2022/10/30
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/86051
 Version: Python 3.10.4
"""

def solution(numbers):
    answer = 0
    for i in range(1, 10):
        if i not in numbers:
            answer += i
        
    return answer