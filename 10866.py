from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

d = deque([])
for _ in range(N):
    comm = input().split()
    if comm[0] == "push_back":
        d.append(comm[1])

    if comm[0] == "push_front":
        d.appendleft(comm[1])

    if comm[0] == "pop_front":
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)

    if comm[0] == "pop_back":
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)

    if comm[0] == "front":
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)

    if comm[0] == "back":
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)

    if comm[0] == "empty":
        print(int(len(d) == 0))

    if comm[0] == "size":
        print(len(d))
