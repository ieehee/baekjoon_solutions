import sys
input = sys.stdin.readline
N = int(input())

todos = []
for _ in range(N):
    T, S = map(int, input().split())
    todos.append([T, S])

todos_sort = sorted(todos, key=lambda x: x[1])

timecost_cumsum = 0
timenotes = []
for todo in todos_sort:
    timecost_cumsum += todo[0]
    if timecost_cumsum > todo[1]:
        print(-1)
        break
    timenotes.append(todo[1] - timecost_cumsum)
else:
    print(min(timenotes))
