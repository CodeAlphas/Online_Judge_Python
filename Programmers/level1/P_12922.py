"""
 프로그래머스: 수박수박수박수박수박수? 풀이
 Author: CodeAlphas
 Date: 2022/10/27
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12922
 Version: Python 3.10.4
"""

def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 == 1:
            answer += '수'
        else:
            answer += '박'
            
    return answer