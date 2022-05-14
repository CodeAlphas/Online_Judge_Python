"""
 백준 10816번: 숫자 카드 2 풀이
 Author: CodeAlphas
 Date: 2022/05/13
 Problem Source: https://www.acmicpc.net/problem/10816
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
s_cards = list(map(int, input().split()))

m = int(input()) 
m_cards = list(map(int, input().split()))

counts = {}
cards_list = set(s_cards + m_cards)

for i in cards_list:
    counts[i] = 0

for card in s_cards:
    counts[card] += 1

for ans in m_cards:
    print(counts[ans], end = ' ')


