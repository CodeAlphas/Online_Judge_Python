"""
 프로그래머스: x만큼 간격이 있는 n개의 숫자 풀이
 Author: CodeAlphas
 Date: 2022/11/10
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12954
 Version: Python 3.10.4
"""

def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)

    return answer