"""
 백준 1541번: 잃어버린 괄호 풀이
 Author: CodeAlphas
 Date: 2022/05/28
 Problem Source: https://www.acmicpc.net/problem/1541
 Version: Python 3.10.4
"""

# 1
# import sys
# input = sys.stdin.readline

# expression = input().rstrip()

# def infixTopostfix(expression):
#     len_exp = len(expression)
#     stack = []; temp = ""; postfix = []
#     ch = False
#     for i in range(len_exp):
#         if expression[i].isnumeric():
#             temp += expression[i]
#         else:
#             postfix.append(temp)
#             if expression[i] == "-":
#                 ch = True
#             if ch:
#                 temp2 = "-"
#             else:
#                 temp2 = expression[i]
#             if stack != []:
#                 postfix.append(stack.pop())
#                 stack.append(temp2)
#             else:
#                 stack.append(temp2)
#             temp = ""
#     postfix.append(temp)
#     while stack != []:
#         postfix.append(stack.pop())
#     return postfix

# def calculateResult(postfix):
#     len_post = len(postfix)
#     stack = []

#     for i in range(len_post):
#         if postfix[i].isnumeric():
#             stack.append(int(postfix[i]))
#         elif postfix[i] == "+":
#             stack.append(stack.pop(-2) + stack.pop(-1))
#         elif postfix[i] == "-":
#             stack.append(stack.pop(-2) - stack.pop(-1))

#     return stack.pop()

# print(calculateResult(infixTopostfix(expression)))

# 2
import sys
input = sys.stdin.readline

expression = input().rstrip().split("-")
num = sum(map(int, expression.pop(0).split("+")))

for exp in expression:
    num -= sum(map(int, exp.split("+")))

print(num)