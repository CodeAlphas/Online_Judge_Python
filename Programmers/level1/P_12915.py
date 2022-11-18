"""
 프로그래머스: 문자열 내 마음대로 정렬하기 풀이
 Author: CodeAlphas
 Date: 2022/11/18
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12915
 Version: Python 3.10.4
"""

def solution(strings, n):
    strings.sort(key = lambda x: (x[n], x))
    return strings