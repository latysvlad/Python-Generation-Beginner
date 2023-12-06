for a in range(1, 33): #3.0-3.6 секунд для верхнего предела перебора переменной "a" в 100 (45 значений)
    for c in range(1, a):
        for d in range(1, c+1):
            for b in range(1, d):
                if a**3 + b**3 == d**3 + c**3:
                    print(a**3+b**3)
