import copy
N = int(input())

Rels = []
for _ in range(N):
    Rel = str(input())

    Rel = Rel.replace("Y", "1")
    Rel = Rel.replace("N", "0")

    Rels.append(list(Rel))

F2s = copy.deepcopy(Rels)
for i in range(N):
    for j in range(N):
        F2s[i][j] = 0
        if i == j:
            F2s[i][j] = F2s[i][j]
            continue
        for k in range(N):
            F2s[i][j] += int(Rels[i][k]) * int(Rels[k][j])
        F2s[i][j] = bool(F2s[i][j]+int(Rels[i][j]))

print(max([sum(x) for x in F2s]))
