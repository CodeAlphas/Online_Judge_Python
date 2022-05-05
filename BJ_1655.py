"""
 1655번: 가운데를 말해요
 Problem Source: https://www.acmicpc.net/problem/1655
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/02.
"""

import sys
import heapq
input = sys.stdin.readline

left_value = []; right_value = []

n = int(input())

for i in range(n):
    number = int(input())

    if i == 0:
        heapq.heappush(left_value, -number)
        print(number)
    else:
        if len(left_value) > len(right_value):
            b = -heapq.heappop(left_value)
            if b > number:
                heapq.heappush(left_value, -number)
                heapq.heappush(right_value, b)
                c = -heapq.heappop(left_value)
                print(c)
                heapq.heappush(left_value, -c)
            else:
                heapq.heappush(right_value, number)
                heapq.heappush(left_value, -b)
                print(b)
        else:
            b = -heapq.heappop(left_value)
            if number <= b:
                heapq.heappush(left_value, -number)
                print(b)
                heapq.heappush(left_value, -b)
            else:
                heapq.heappush(left_value, -b)
                c = heapq.heappop(right_value)
                if number >= c:
                    print(c)
                    heapq.heappush(left_value, -c)
                    heapq.heappush(right_value, number)
                else:
                    print(number)
                    heapq.heappush(left_value, -number)
                    heapq.heappush(right_value, c)

                
    