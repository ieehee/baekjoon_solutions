M, N = map(int, input().split())

is_prime = [0, 0] + [1]*(N-1)
for i in range(2, N+1):
    if is_prime[i]:
        for j in range(2*i, N+1, i):
            is_prime[j] = 0
for i in range(M, N+1):
    if is_prime[i]:
        print(i)
