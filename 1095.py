import math

S, F, M = map(int, input().split())


def find_exponent(num, x):
    exp = 0
    while num >= x:
        exp += num//x
        num = num//x
    return exp


def find_prime(num):
    primes = [0, 0] + [1]*(num-1)
    n_primes = []
    for i in range(2, num):
        if primes[i]:
            for j in range(i*2, num+1, i):
                primes[j] = 0
    for i in range(len(primes)):
        if primes[i]:
            n_primes.append(i)
    return n_primes


def find_maxdivisor(num, n_primes, exps):
    nums = [x for x in range(0, num+1)]
    for exp, prime in zip(exps, n_primes):
        temp = 1
        while temp <= exp and prime*temp < num+1:
            for j in range(prime**temp, num+1, prime**temp):
                nums[j] = nums[j]//prime
            temp += 1
    for n in range(num, 0, -1):
        if nums[n] == 1:
            return n
    return -1


n_p = find_prime(M)
exps = [0]*len(n_p)
for i, prime in enumerate(n_p):
    exps[i] = find_exponent(S+F, prime) \
        - find_exponent(S, prime) \
        - find_exponent(F, prime)

print(find_maxdivisor(M, n_p, exps))
