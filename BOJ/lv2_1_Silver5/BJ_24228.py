"""
 백준 24228번: 젓가락 풀이
 Author: CodeAlphas
 Date: 2022/05/23
 Problem Source: https://www.acmicpc.net/problem/24228
 Version: Python 3.10.4
"""

n, r = map(int, input().split())
print(2 * r + n - 1) # 계차수열