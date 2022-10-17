"""
 프로그래머스: 이중우선순위큐 풀이
 Author: CodeAlphas
 Date: 2022/10/17
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42628
 Version: Python 3.10.4
"""

from heapq import heappop, heappush

def solution(operations):
    answer = []; min_heap = []; max_heap = []
    
    for operation in operations:
        op, num = map(str, operation.split()); num = int(num)
        if op == "I": 
            heappush(min_heap, num)
            heappush(max_heap, -num)
        elif op == "D" and min_heap: 
            if num == 1: 
                temp = heappop(max_heap)
                min_heap.remove(-temp)
            else: 
                temp = heappop(min_heap)
                max_heap.remove(-temp)
            
    if not min_heap: answer = [0, 0]
    else: answer = [-heappop(max_heap), heappop(min_heap)]
    
    return answer