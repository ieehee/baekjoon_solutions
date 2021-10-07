from collections import deque
N, M = map(int, input().split())


to_pulls = list(map(int, input().split()))


def rotate(d):
    d.append(d.popleft())


d = deque([x for x in range(1, N+1)])

move = 0
for i in to_pulls:
    count = 0
    while i != d[0]:
        rotate(d)
        count += 1
    d.popleft()
    count = min(count, N-count)
    N -= 1
    move += count

print(move)
