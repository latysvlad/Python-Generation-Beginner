n, prod, tot = int(input()), 1, 0

for i in range(1, n + 1):
    prod *= i
    tot += prod
    
print(tot)
