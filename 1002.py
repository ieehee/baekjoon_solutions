T = int(input())

todos = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d == int(d):
        d = int(d)
    if r2 > r1:
        todos.append([d, r1, r2])
        continue
    todos.append([d, r2, r1])


def check(todo):
    if todo[0] == 0 and todo[1] == todo[2]:
        return -1
    if todo[0] == todo[2]:
        return 2
    if todo[0] < todo[2]:
        if todo[0]+todo[1] < todo[2]:
            return 0
        elif todo[0]+todo[1] == todo[2]:
            return 1
    else:
        if todo[0]-todo[1] > todo[2]:
            return 0
        elif todo[0]-todo[1] == todo[2]:
            return 1
    return 2


for todo in todos:
    print(check(todo))
