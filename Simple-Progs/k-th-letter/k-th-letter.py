n = int(input())
spisok = list()
stroka = ""

for _ in range(n):
    spisok.append(input())

k = int(input())
for s in spisok:
    if len(s) >= k:
        stroka += s[k - 1]

print(stroka)
