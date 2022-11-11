"""
 프로그래머스: 제일 작은 수 제거하기 풀이
 Author: CodeAlphas
 Date: 2022/11/11
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12935
 Version: Python 3.10.4
"""

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
    else:
        arr = [-1]
    
    return arr