"""
 프로그래머스: 하샤드 수 풀이
 Author: CodeAlphas
 Date: 2022/09/28
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12947
 Version: Python 3.10.4
"""

def solution(x):
    n = 0
    x = str(x)
    for i in range(len(x)):
        n += int(x[i])
    
    if int(x) % n == 0: return True 
    else: return False