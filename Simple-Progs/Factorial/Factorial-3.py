from math import factorial

n, tot = int(input()), 0

for i in range(1, n + 1):
    tot += factorial(i)   
    
print(tot)
