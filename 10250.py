T = int(input())

todos = []
for i in range(T):
    H, W, N = map(int, input().split())
    todos.append([H, W, N])

for todo in todos:
    floor = todo[2] % todo[0]
    if floor == 0:
        floor = todo[0]
    print(str(floor) + "{:02d}".format((todo[2]-1)//todo[0]+1))
