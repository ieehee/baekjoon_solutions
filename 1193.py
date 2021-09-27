X = int(input())
i = 1
cut = 1
while X - cut > 0:
    i += 1
    cut += i
left = X - (cut - i)
if i % 2 == 0:  # descending
    print(str(left)+"/"+str(i-(left-1)))
else:  # ascending
    print(str(i-(left-1))+"/"+str(left))
