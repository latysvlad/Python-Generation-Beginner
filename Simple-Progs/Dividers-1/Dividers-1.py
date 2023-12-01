a, b = int(input()), int(input())
mx_div_num = 0
mx_div_tot = 0

for i in range(a, b+1):
    div_tot = 0
    for j in range(1, i+1):
        if i % j == 0:
            div_tot += j
    if div_tot > mx_div_tot:
        mx_div_num = i
        mx_div_tot = div_tot
    if div_tot == mx_div_tot:
        mx_div_num = max(i, mx_div_num)

print(mx_div_num, mx_div_tot)
