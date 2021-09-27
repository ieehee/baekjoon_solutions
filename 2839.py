
N = int(input())

if N % 5 == 0:
    print(N//5)
elif N % 5 == 3:
    print(N//5+1)
elif N >= 6 and N % 5 == 1:
    print(N//5+1)
elif N >= 9 and N % 5 == 4:
    print(N//5+2)
elif N >= 12 and N % 5 == 2:
    print(N//5+2)
else:
    print(-1)
