"""
 2164번: 카드2
 Problem Source: https://www.acmicpc.net/problem/2164
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/05.
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1, n+1)])

def solution(cards):
    while(len(cards) != 1):
        # cards.remove(cards[0])
        cards.popleft()
        temp = cards.popleft()
        cards.append(temp)

solution(cards)
print(cards[0])

