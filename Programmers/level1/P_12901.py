"""
 프로그래머스: 2016년 풀이
 Author: CodeAlphas
 Date: 2022/11/03
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12901
 Version: Python 3.10.4
"""

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["FRI","SAT", "SUN", "MON", "TUE", "WED", "THU"]

def solution(a, b):
    answer = ''
    for i in range(a-1):
        b += days[i]
    answer = day[(b-1) % 7] 
    
    return answer