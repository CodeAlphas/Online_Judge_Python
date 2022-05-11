"""
 백준 11866번: 요세푸스 문제 0 풀이
 Author: CodeAlphas
 Date: 2022/05/11
 Problem Source: https://www.acmicpc.net/problem/11866
 Version: Python 3.10.4
"""

n, k = map(int, input().split())
circles = [i for i in range(1, n+1)]
results = []
index = k - 1

while n:
    n -= 1
    results.append(str(circles.pop(index)))
    index += (k - 1)
    try:
        index %= n
    except:
        break

print('<' + ', '.join(results) + '>')    