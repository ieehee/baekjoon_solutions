import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

keeper = []
NGEs = [-1]*N

for i in range(N):
    while len(keeper) != 0 and A[i] > A[keeper[-1]]:
        NGEs[keeper[-1]] = A[i]
        keeper.pop()
    keeper.append(i)

print(*NGEs)
