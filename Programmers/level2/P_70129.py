"""
 프로그래머스: 이진 변환 반복하기 풀이
 Author: CodeAlphas
 Date: 2022/11/02
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/70129
 Version: Python 3.10.4
"""

def conversion(x):
    count = x.count('0')
    x = x.split('0')
    x = "".join(x)
    x = format(len(x), 'b')
    
    return x, count
    
def solution(s):
    c, zc = 0, 0
    while s != '1':
        c += 1
        s, t = conversion(s)
        zc += t
        
    return [c, zc]