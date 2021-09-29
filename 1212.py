N = str(input())
b = ""
for i, c in enumerate(N):
    cb = bin(int(c))[2:]
    if i != 0:
        while len(cb) < 3:
            cb = "0"+cb
    b += cb

print(b)
