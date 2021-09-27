import sys
import math
input = sys.stdin.readline

T = int(input())

Ds = []
for i in range(T):
    x, y = map(int, input().split())
    Ds.append(y-x)

for D in Ds:
    D_isqrt = math.isqrt(D)
    if D_isqrt**2 == D:
        print(2*D_isqrt-1)
    elif D_isqrt**2+D_isqrt < D:
        print(2*D_isqrt+1)
    else:
        print(2*D_isqrt)
