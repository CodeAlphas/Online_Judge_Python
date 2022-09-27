"""
 프로그래머스: N개의 최소공배수 풀이
 Author: CodeAlphas
 Date: 2022/09/27
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12953
 Version: Python 3.10.4
"""

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)
            
    return answer