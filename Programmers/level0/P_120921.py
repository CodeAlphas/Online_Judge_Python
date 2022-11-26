"""
 프로그래머스: 문자열 밀기 풀이
 Author: CodeAlphas
 Date: 2022/11/26
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/120921
 Version: Python 3.10.4
"""

from collections import deque

def solution(A, B):
    answer = 0
    q_a, q_b = deque(list(A)), deque(list(B))
    
    for i in range(len(A)):
        if q_a == q_b:
            return answer
        q_a.appendleft(q_a.pop())
        answer += 1
    return -1