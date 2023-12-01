n = int(input())
tot = 0

for i in range(1, n + 1):
    prod = 1
    for j in range(1, i + 1):
        prod *= j
    tot += prod

print(tot)
