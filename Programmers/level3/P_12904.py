"""
 프로그래머스: 가장 긴 팰린드롬 풀이
 Author: CodeAlphas
 Date: 2022/10/21
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12904
 Version: Python 3.10.4
"""

def check(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1; right += 1
        
    return len(s[left+1:right])

def solution(s):
    answer = 0
    if len(s) == 1: return 1
    for i in range(len(s)-1):
        answer = max(answer, check(s, i, i), check(s, i, i+1))
        
    return answer