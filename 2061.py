# 런타임에러 OverFlow error
# -> K**0.5 대신 L까지 조회해서 해결
# also submitted for other same prob. #1xxx

import sys
input = sys.stdin.readline

K, L = map(int, input().split())

a = [False, False] + [True]*(L-1)
primes = []

for i in range(2, L):
    if a[i]:
        primes.append(i)
        for j in range(2*i, L, i):
            a[j] = False

check = 1
for prime in primes:
    if K % prime == 0:
        print("BAD " + str(prime))
        check = 0
        break
if check:
    print("GOOD")
