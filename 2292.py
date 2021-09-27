N = int(input())
lim = 1
i = 1
while N - lim > 0:
    lim += 6*i
    i += 1
print(i)
