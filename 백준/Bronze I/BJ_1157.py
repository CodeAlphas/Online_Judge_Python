"""
 백준 1157번: 단어 공부 풀이
 Author: CodeAlphas
 Date: 2022/04/17
 Problem Source: https://www.acmicpc.net/problem/1157
 Version: Python 3.10.4
"""

# 1
# s = input()

# alphabet = [i for i in range(65, 91)] 
# max_alphabet_count = 0

# for i in alphabet:
#     if max_alphabet_count < s.count(chr(i)) + s.count(chr(i+32)):
#         max_alphabet_count = s.count(chr(i)) + s.count(chr(i+32))
#         max_alphabet = chr(i)
#     elif max_alphabet_count == s.count(chr(i)) + s.count(chr(i+32)):
#         max_alphabet = '?'

# print(max_alphabet)

# 2
s = input().lower()
ss = list(set(s))
cnt = []

for i in ss:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(ss[cnt.index(max(cnt))].upper())
