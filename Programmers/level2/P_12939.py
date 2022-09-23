"""
 프로그래머스: 최댓값과 최솟값 풀이
 Author: CodeAlphas
 Date: 2022/09/23
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12939
 Version: Python 3.10.4
"""

def solution(s):
    num_list = list(map(int, s.split()))
    return f"{str(min(num_list))} {str(max(num_list))}"