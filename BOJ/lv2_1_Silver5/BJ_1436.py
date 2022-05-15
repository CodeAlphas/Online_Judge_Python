"""
 백준 1436번: 영화감독 숌 풀이
 Author: CodeAlphas
 Date: 2022/05/14
 Problem Source: https://www.acmicpc.net/problem/1436
 Version: Python 3.10.4
"""

# 1
# n = int(input())
# check_n = 0

# num_list = [str(i) for i in range(666, 3000000)]

# for i in num_list:
#     if '666' in i:
#         check_n += 1
#         if n == check_n:
#             print(i)
#             break
    
# 2
n = int(input())
check_n = 0
start_n = 666

while n != check_n:
    if '666' in str(start_n):
        check_n += 1
    start_n += 1
        
print(start_n - 1)