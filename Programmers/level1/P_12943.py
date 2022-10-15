"""
 프로그래머스: 콜라츠 추측 풀이
 Author: CodeAlphas
 Date: 2022/10/15
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12943
 Version: Python 3.10.4
"""

def check(num, count):
    if num == 1: return count
    if num % 2 == 0: c = check(num // 2, count + 1)
    else: c = check(3 * num + 1, count + 1)
    return c

def solution(num):
    answer = check(num, 0)
    if answer >= 500: answer = -1
    return answer