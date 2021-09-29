# Working

N = int(input())

Rels = []
for _ in range(N):
    Rel = str(input())

    Rel = Rel.replace("Y", "1")
    Rel = Rel.replace("N", "0")

    Rels.append(Rel)

F2s = [[0]*N]*N
for i in range(N):
    for j in range(N):
        F2s[i][j] = 0
        if i == j:
            continue
        for k in range(N):
            F2s[i][j] += int(Rels[i][k]) * int(Rels[k][j])
        F2s[i][j] = bool(F2s[i][j])
print(max([sum(x) for x in F2s]))
