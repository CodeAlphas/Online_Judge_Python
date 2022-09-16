"""
 프로그래머스: 카펫 풀이
 Author: CodeAlphas
 Date: 2022/09/16
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42842
 Version: Python 3.10.4
"""

def solution(brown, yellow):
    answer = []
    num = brown + yellow
    
    temp = []; i = 1; last = int(num ** 0.5)
    while i <= last: 
        if num % i == 0:
            temp += [[num // i, i]]
        i += 1
    
    n = len(temp)
    for i in range(n-1, -1, -1):
        a, b = temp[i]
        if a * 2 + (b - 2) * 2 == brown:
            answer = [a, b]
            break
        
    return answer