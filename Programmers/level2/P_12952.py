"""
 프로그래머스: N-Queen 풀이
 Author: CodeAlphas
 Date: 2022/10/20
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12952
 Version: Python 3.10.4
"""

def check(x, count, queens):
    for qx, qy in queens:
        if x == qx: return False
        elif abs(qx - x) == abs(qy - count): return False

    return True
    
def b_tracking(n, count, queens):
    global answer
    if count == n:
        answer += 1
        return
    
    for x in range(n):
        if check(x, count, queens):
            b_tracking(n, count+1, queens + [(x, count)])

answer = 0
def solution(n):
    b_tracking(n, 0, [])
    return answer