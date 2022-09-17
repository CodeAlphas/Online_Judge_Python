"""
 프로그래머스: H-Index 풀이
 Author: CodeAlphas
 Date: 2022/09/17
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42747
 Version: Python 3.10.4
"""

def solution(citations):
    answer = 0
    
    for h in range(1, 1001):
        num = 0
        for c in citations:
            if c >= h:
                num += 1
                if num >= h:
                    answer = max(answer, h)
                    break
                
    return answer