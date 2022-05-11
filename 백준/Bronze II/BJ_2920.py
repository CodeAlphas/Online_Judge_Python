"""
 백준 2920번: 음계 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/2920
 Version: Python 3.10.4
"""

play = list(map(int, input().split()))
ascend = 1; check_as = True
descend = 8; check_des = True

for note in play:
    if note == ascend and check_as:
        ascend += 1
        check_des = False
    elif note == descend and check_des:
        descend -= 1
        check_as = False
    else:
        print("mixed")
        break
    if check_as and ascend == 9:
        print("ascending")
    elif check_des and descend == 0:
        print("descending")
