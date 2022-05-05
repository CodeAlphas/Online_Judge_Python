"""
 1193번: 분수찾기
 Problem Source: https://www.acmicpc.net/problem/1193
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/18.
"""

x = int(input())
n = 1

while x > (n * n + n) / 2:
    n += 1

tx = x - (((n-1) * (n-1) + (n-1)) // 2)

if n % 2 == 0:
    result = str(tx) + '/' + str((n + 1) - tx)
else:
    result = str((n + 1) - tx) + '/' + str(tx)

print(result)