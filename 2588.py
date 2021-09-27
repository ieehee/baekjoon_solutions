
A = int(input())
B = int(input())

l3 = A*(B % 10)
l4 = A*(B % 100//10)
l5 = A*(B//100)
print(l3)
print(l4)
print(l5)
print(l3+l4*10+l5*100)
