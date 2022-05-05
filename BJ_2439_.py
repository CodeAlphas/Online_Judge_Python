"""
print('m'+'n') # mn
print('m','n') # m n
문자열 합성시 +의 경우에는 공백 없이 합쳐짐. 
반면 ,의 경우에는 공백이 추가되어 합쳐짐
"""

n = int(input())

for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)