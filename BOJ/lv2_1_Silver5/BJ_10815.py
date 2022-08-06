"""
 백준 10815번: 숫자 카드 풀이
 Author: CodeAlphas
 Date: 2022/07/17
 Problem Source: https://www.acmicpc.net/problem/10815
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards_dict = {}
for card in cards:
    cards_dict[card] = 1

m = int(input())
ch_cards = list(map(int, input().split()))

for card in ch_cards:
    if card in cards_dict:
        print(1, end = " ")
    else:
        print(0, end = " ")
