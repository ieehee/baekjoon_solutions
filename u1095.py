# Working

import math

S, F, M = map(int, input().split())
# 1G, 1G, 0.1M
# n*(n-1)*(n-2)/1/2/3
T = math.comb(S+F, S)
# max 10^(9*9+8*9+7*9+6*9+5*9)

if min(S, F) > M:
    print(M)
else:
    for i in range(2, M):
        if T % i == 0:
            print(i)
            break
    print(-1)
