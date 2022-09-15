"""
 프로그래머스: JadenCase 문자열 만들기 풀이
 Author: CodeAlphas
 Date: 2022/09/15
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12951
 Version: Python 3.10.4
"""

def solution(s):
    answer = ''
    last = len(s)
    ch = True
    
    for i in range(0, last):
        if s[i] == " ":
            answer += s[i]
            ch = True
        else:
            if ch:
                if s[i].isalpha():
                    answer += s[i].upper()
                else:
                    answer += s[i]
                ch = False
            else:
                answer += s[i].lower()
    
    return answer