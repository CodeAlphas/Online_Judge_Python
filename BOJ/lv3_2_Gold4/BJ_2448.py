"""
 백준 2448번: 별 찍기 - 11 풀이
 Author: CodeAlphas
 Date: 2022/06/27
 Problem Source: https://www.acmicpc.net/problem/2448
 Version: Python 3.10.4
"""

import math
import copy
n = int(input())
k = int(math.log2(n//3))

def printStar(n, result):
    if n == k:
        for star in result:
            print(star)
        return
    else:
        for _ in range(1):
            temp = []; blank = 3 * 2 ** (n+1) // 2
            for i in result:
                temp.append(" " * blank + i + " " * blank)
            for i in result:
                temp.append(i + " " + i)
        result = copy.deepcopy(temp)
        printStar(n+1, result)

printStar(0, ["  *  "," * * ", "*****"])