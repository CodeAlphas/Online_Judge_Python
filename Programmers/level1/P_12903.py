"""
 프로그래머스: 가운데 글자 가져오기 풀이
 Author: CodeAlphas
 Date: 2022/09/29
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12903
 Version: Python 3.10.4
"""

def solution(s):
    answer = '' 
    s_len = len(s)
    if s_len % 2 == 0:
        answer = s[s_len//2 - 1] + s[s_len//2] 
    else:
        answer = s[s_len//2]
    
    return answer