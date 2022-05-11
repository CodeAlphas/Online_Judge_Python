"""
 백준 2941번: 크로아티아 알파벳 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/2941
 Version: Python 3.10.4
"""

# 1
# s = input()
# count = 0

# for i in range(len(s)):
#     if s[i] == '=':
#         if s[i-1] in ['c', 's']:
#             continue
#         elif s[i-1] == 'z':
#             if s[i-2] == 'd':
#                 count -= 1
#             continue
#     elif s[i] == '-':
#         if s[i-1] in ['c', 'd']:
#             continue
#     elif s[i] == 'j':
#         if s[i-1] in ['l', 'n']:
#             continue 
#     count += 1

# print(count)
 
# 2
s = input()
count = 0
array = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in array:
    if i in s:
        count += s.count(i)
        s = s.replace(i, ' ')
s = s.replace(' ', '')
print(count + len(s))


