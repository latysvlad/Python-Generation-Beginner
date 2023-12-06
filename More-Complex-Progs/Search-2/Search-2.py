n = int(input())

stroki = []
for _ in range(n):
    stroki.append(input())

k = int(input())

zapros = []
for _ in range(k):
    zapros.append(input())

for el_1 in stroki:
    for el_2 in zapros:
        if el_2.lower() not in el_1.lower():
            break
    else:
        print(el_1)
