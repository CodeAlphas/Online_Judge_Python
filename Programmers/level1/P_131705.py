"""
 프로그래머스: 삼총사 풀이
 Author: CodeAlphas
 Date: 2022/11/04
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/131705
 Version: Python 3.10.4
"""

from itertools import combinations

def solution(number):
    answer = 0
    number_list = list(combinations(number, 3))
    for numbers in number_list:
        if sum(numbers) == 0:
            answer += 1
    
    return answer