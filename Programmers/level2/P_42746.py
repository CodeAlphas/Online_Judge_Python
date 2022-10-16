"""
 프로그래머스: 가장 큰 수 풀이
 Author: CodeAlphas
 Date: 2022/10/16
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42746
 Version: Python 3.10.4
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda i:i*4, reverse = True)
    answer = str(int(("").join(numbers)))
    return answer