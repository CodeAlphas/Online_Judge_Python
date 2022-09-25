"""
 프로그래머스: 소수 찾기 풀이
 Author: CodeAlphas
 Date: 2022/09/25
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42839
 Version: Python 3.10.4
"""

from itertools import permutations

def isPrimeNumber(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    m_numbers = []
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for t in temp:
            m_numbers.append(int("".join(t)))
            
    m_numbers = set(m_numbers)
    for num in m_numbers:
        if isPrimeNumber(num):
            answer += 1
        
    return answer