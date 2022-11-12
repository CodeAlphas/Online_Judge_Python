"""
 프로그래머스: 숫자 짝꿍 풀이
 Author: CodeAlphas
 Date: 2022/11/12
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/131128
 Version: Python 3.10.4
"""

def solution(X, Y):
    answer = ""
    x = {}; y = {}
    for num in X:
        x[num] = x.get(num, 0) + 1
    for num in Y:
        y[num] = y.get(num, 0) + 1
    
    c = x.keys() & y.keys()
    sc = sorted(c, reverse = True)
    for num in sc:
        answer += min(x[num], y[num]) * num
    
    if answer == "":
        answer = "-1"
    if sc == ['0']:
        answer = "0"
    return answer