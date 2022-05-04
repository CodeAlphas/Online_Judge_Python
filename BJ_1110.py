"""
 1110번: 더하기 사이클
 Problem Source: https://www.acmicpc.net/problem/1110
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/17.
"""

# 1
# n = input()
# result = n
# count = 0

# while True:
#     if int(n) < 10:
#         n = int(n)
#         n = '0' + str(n)

#     tn = int(n[0]) + int(n[1])

#     if tn < 10:
#         tn = '0' + str(tn)

#     tn = str(tn)
#     nn = n[1] + tn[1]
#     count += 1

#     if int(nn) == int(result):
#         break
#     n = nn

# print(count)

# 2
n = int(input())
org = n
count = 0 

while True:
    fn = n - (10 * (n // 10))
    sn = (n // 10) + fn
    nn = fn * 10 + (sn - (10 * (sn // 10)))
    n = nn
    count += 1

    if org == n:
        break

print(count)