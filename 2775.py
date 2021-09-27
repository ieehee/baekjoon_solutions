import math
T = int(input())

todos = []
for i in range(T):
    k = int(input())
    n = int(input())
    todos.append([k, n])

# timeover solutions
# def solution(k, n):
#     if k == 0:
#         return n
#     else:
#         return sum([solution(k-1, i) for i in range(1, n+1)])
# def solution(k, n):
#     if k == 0:
#         return n
#     if n == 1:
#         return 1
#     return solution(k-1, n) + solution(k, n-1)

for todo in todos:
    print(math.comb(todo[0]+todo[1], todo[1]-1))
