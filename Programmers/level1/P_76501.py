"""
 프로그래머스: 음양 더하기 풀이
 Author: CodeAlphas
 Date: 2022/11/06
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/76501
 Version: Python 3.10.4
"""

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer