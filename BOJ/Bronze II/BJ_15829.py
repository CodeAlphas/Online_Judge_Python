"""
 백준 15829번: Hashing 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/15829
 Version: Python 3.10.4
"""

def hash(a, l):
    hash_num = 0
    for i in range(l):
        hash_num += (ord(a[i]) - 96) * (31 ** i)
    return hash_num % 1234567891


l = int(input()) # 문자열의 길이
string = input()

print(hash(string, l))

