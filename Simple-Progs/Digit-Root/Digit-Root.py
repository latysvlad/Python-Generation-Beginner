n = int(input())

while n > 9:
    sum_digit = 0
    while n:
        sum_digit += n % 10
        n //= 10
        
    n = sum_digit

print(n)
