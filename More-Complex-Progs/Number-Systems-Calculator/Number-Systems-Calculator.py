def convert_to_decimal(num, base):
    tot = 0
    grade = 0
    if base > 10:
        flag = True
    else:
        flag = False
    while num:
        el = num[-1]
        if flag and el not in "0123456789":
            el = base_above_decimal_to(el)
        else:
            el = int(el)
        tot += el * base ** grade
        grade += 1
        num = num[:-1]
    return tot


def convert_from_decimal(num, base):
    result = []
    if base > 10:
        flag = True
    else:
        flag = False
    while True:
        el = num % base
        if flag and el > 9:
            el = base_above_decimal_from(el)
        result.append(str(el))
        if num == num % base:
            break
        else:
            num //= base
    result.reverse()
    return "".join(result)


def base_above_decimal_to(num):
    more_than_ten = ["A", "B", "C", "D", "E", "F"]
    res_num = 10 + more_than_ten.index(num)
    return int(res_num)


def base_above_decimal_from(num):
    more_than_ten = ["A", "B", "C", "D", "E", "F"]
    res_num = more_than_ten[num - 10]
    return res_num


old_num = input("Введите исходное число\n")
old_base = int(input("Введите основание системы счисления исходного числа\n"))
new_base = int(input("Введите основание системы для перевода\n"))

if old_base == new_base:
    print(old_num)
elif old_base == 10:
    print(convert_from_decimal(int(old_num), new_base))
elif new_base == 10:
    print(convert_to_decimal(old_num, old_base))
else:
    print(convert_from_decimal(convert_to_decimal(old_num, old_base), new_base))


