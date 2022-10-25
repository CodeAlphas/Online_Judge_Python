"""
 프로그래머스: 입국심사 풀이
 Author: CodeAlphas
 Date: 2022/10/23
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/43238
 Version: Python 3.10.4
"""

def solution(n, times):
    left = 1; right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        num = 0
        for t in times:
            num += mid // t
            
        if num >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer