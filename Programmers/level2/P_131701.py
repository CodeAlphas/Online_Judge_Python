"""
 프로그래머스: 연속 부분 수열 합의 개수 풀이
 Author: CodeAlphas
 Date: 2022/10/28
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/131701
 Version: Python 3.10.4
"""

def solution(elements):
    len_e = len(elements)
    elements = 2 * elements
    numbers = []
    for lenth in range(1, len_e + 1):
        for idx in range(len_e):
            numbers.append(sum(elements[idx:idx+lenth]))
    numbers = set(numbers)
    
    return len(numbers)