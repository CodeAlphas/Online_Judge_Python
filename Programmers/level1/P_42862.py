"""
 프로그래머스: 체육복 풀이
 Author: CodeAlphas
 Date: 2022/11/09
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42862
 Version: Python 3.10.4
"""

def solution(n, lost, reserve):
    n_lost = list(set(lost) - set(reserve))
    n_reserve = list(set(reserve) - set(lost))
    answer = n - len(n_lost)
    
    for i in n_lost:
        front = i - 1; back = i + 1
        if front in n_reserve:
            answer += 1
            n_reserve.remove(front)
            continue
        if back in n_reserve:
            answer += 1
            n_reserve.remove(back)
            
    return answer