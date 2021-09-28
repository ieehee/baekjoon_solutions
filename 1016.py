A, B = map(int, input().split())

if B < 4:
    print(0)
else:
    is_snn = [1] * (B-A+1)  # maxsize=1M
    intB_sqrt = int(B**0.5)
    checker = [0, 0] + [1] * (intB_sqrt-1)  # maxsize=1M

    for i in range(2, intB_sqrt+1):  # <1M run
        if checker[i]:
            tmp = A % (i**2)
            if tmp == 0:
                tmp = i**2
            for j in range(i**2 - tmp, B-A+1, i**2):  # <=0.25M per run
                is_snn[j] = 0
            for j in range(i**2, intB_sqrt+1, i**2):  # <=0.25M per run
                checker[j] = 0

    print(sum(is_snn))
