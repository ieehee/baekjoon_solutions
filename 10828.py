import sys
input = sys.stdin.readline

clines = int(input())
stack = []

for i in range(clines):
    command = input().split()

    if command[0] == "push":
        stack.append(command[1])
        continue

    if command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
        continue

    if command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        continue

    if command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        continue

    if command[0] == "size":
        print(len(stack))
        continue
