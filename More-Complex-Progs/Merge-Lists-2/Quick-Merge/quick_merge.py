def quick_merge(list1, list2):      # функция для объединения двух списков в отсортированный список
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


def result_list_creation(data_set, length):     # функция для создания общего списка из всех входных данных, где data_set - список со списками чисел, n - число подаваемых строк (длина data_set)
    result = []
    result.extend(data_set[0])  # создаем заготовку результирующего списка

    for i in range(1, length):
        result = quick_merge(result, data_set[i])     # добавляем постепенно остальные списки нащей сортировочной функцией

    return result


n = int(input())
sorted_lists = []  # создаем пустой список для ввода отсортированных списков чисел

for _ in range(n):
    sorted_lists.append([int(c) for c in input().split()])  # формируем список входных данных, вводя n строк с числами с последующим разбиением на списки

result_list = result_list_creation(sorted_lists, n)

print(*result_list)
