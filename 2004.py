N, M = map(int, input().split())


def find_iexponent(num, base):
    exp = 0
    while num >= base:
        exp += num//base
        num //= base
    return exp


exp_5 = find_iexponent(N, 5) - find_iexponent(N-M, 5) - find_iexponent(M, 5)
exp_2 = find_iexponent(N, 2) - find_iexponent(N-M, 2) - find_iexponent(M, 2)

print(int(min(exp_5, exp_2)))
