import sys
input = sys.stdin.readline
T = int(input())

cases = []
for i in range(T):
    cases.append(int(input()))
memo = [0, 1, 1]
for n in cases:
    if n == 0:
        print(1, 0)
        continue
    elif len(memo) < n + 1:
        while len(memo) < n + 1:
            memo.append(memo[-1]+memo[-2])
    print(memo[n-1], memo[n])
