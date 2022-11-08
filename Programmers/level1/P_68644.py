"""
 프로그래머스: 두 개 뽑아서 더하기 풀이
 Author: CodeAlphas
 Date: 2022/11/08
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/68644
 Version: Python 3.10.4
"""

def solution(numbers):
    answer = []
    len_numbers = len(numbers)
    for i in range(len_numbers - 1):
        for j in range(i + 1, len_numbers):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    
    return answer