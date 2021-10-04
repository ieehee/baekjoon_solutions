
N = int(input())

d_Ns = []
search = 0
#counter = 0
if N > 1022:
    d_Ns = [-1]*(N+1)

while len(d_Ns) <= N:
    n_str = str(search)
    n_p = 10
    for i, n in enumerate(n_str):
        #counter += 1
        if int(n_p)-int(n) <= 0:
            n_str = n_str[:i-1]+str(int(n_p+1))+"0"*(len(n_str)-i)
            search = int(n_str)
            break
        n_p = int(n)
        if i == len(n_str)-1:
            d_Ns.append(search)
            search += 1


print(d_Ns[-1])
