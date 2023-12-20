from random import randint
import time     # импорт библиотеки для анализа времени работы программы
start = time.time()     # стартовая точка отсчета


def quick_merge(list1, list2):      # функция 1
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    if i < len(list1):
        result.extend(list1[i:])
    else:
        result.extend(list2[j:])

    return result


def pop_merge(list1, list2):        # функция 2
    result = []

    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    if list1:
        result.extend(list1)
    else:
        result.extend(list2)

    return result


def reverse_pop_merge(list1, list2):        # функция 3
    result = []
    while list1 and list2:
        result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
    return list1 + list2 + result[::-1]


def sort_merge(list1, list2):       # функция 4
    result = (list1 + list2)
    result.sort()
    return result


minlen, maxlen = 50000, 50000    # обозначение интервала для выбора длины списков - для упрощения анализа границы одинаковые
minval, maxval = 1, 100000       # интервал выбора значений элементов списков
n = 5                            # количество списков
result_list = []

for _ in range(n):
    length = randint(minlen, maxlen)
    result_list = sort_merge(result_list, sorted([randint(minval, maxval) for __ in range(length)]))   # создание и сразу же сортировка n списков чисел

print(*result_list)     # вывод результирующего списка


end = time.time() - start        # конечная точка
print('\n', end)        # вывод полученного результата времени

# Анализ результатов:

# для 5000 и 2 списков:
    # pop_merge - 0.034 - 0.050
    # quick_merge - 0.032 - 0.047
    # reverse_pop_merge 0.032 - 0.047
    # sort_merge 0.030 - 0.045

# для 50000 и 2 списков:
    # quick_merge - 0.35 - 0.44
    # pop_merge - 0.64 - 0.74
    # reverse_pop_merge 0.35 - 0.45
    # sort_merge 0.32 - 0.43

# для 50000 и 5 списков:
    # quick_merge - 1.07 - 1.28
    # pop_merge - 6.95 - 7.05
    # reverse_pop_merge 1.02 - 1.23
    # sort_merge 0.89 - 1.11
