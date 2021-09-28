N = int(input())

temp = int(N)
i = 2
is_prime = True
if N == 1:
    is_prime = False
for i in range(2, N//2+1):
    if temp % i == 0:
        is_prime = False
        while temp % i == 0:
            temp = temp//i
            print(i)
if is_prime:
    print(N)
