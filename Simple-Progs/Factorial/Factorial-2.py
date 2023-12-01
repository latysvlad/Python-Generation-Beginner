n = int(input())
prod = 1
tot = 0

for i in range(1, n + 1):
    prod *= i
    tot += prod
    
print(tot)
