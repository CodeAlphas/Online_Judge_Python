import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
GI = []
GP = []

for i in range(P):
    GI.append(int(sys.stdin.readline()))

for j in range(P):
    if GI[j] not in GP:
        GP.append(GI[j])

print(len(GP))
