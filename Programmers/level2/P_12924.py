"""
 프로그래머스: 숫자의 표현 풀이
 Author: CodeAlphas
 Date: 2022/11/14
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12924
 Version: Python 3.10.4
"""

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        sum_num = 0
        for j in range(i, n + 1):
            sum_num += j
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
    
    return answer