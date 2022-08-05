"""
 백준 2447번: 별 찍기 - 10 풀이
 Author: CodeAlphas
 Date: 2022/07/16
 Problem Source: https://www.acmicpc.net/problem/2447
 Version: Python 3.10.4
"""

n = int(input())

def printStar(depth, stars):
    if depth == n:
        for star in stars:
            print(star)
        return
    else:
        t_stars = []
        for i in range(3):
            if i == 1:
                for star in stars:
                    t_stars.append(star + " " * depth + star)
            else:
                for star in stars:
                    t_stars.append(star * 3)
        printStar(depth*3, t_stars)

printStar(3, ["***", "* *", "***"])