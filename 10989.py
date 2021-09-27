
import sys
input = sys.stdin.readline

N = int(input())
nums = [0]*10001
for i in range(N):
    num = int(input())
    nums[num] += 1

for i, n in enumerate(nums):
    if i == 0:
        continue
    for j in range(n):
        print(i)
