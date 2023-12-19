def reverse_pop_merge(list1, list2):      # функция для объединения двух списков в отсортированный список
    result = []
    while list1 and list2:
        result.append((list1 if list1[-1] > list2[-1] else list2).pop(-1))
    return list1 + list2 + result[::-1]


n = int(input())
result_list = []    # создаем заготовку результирующего списка

for _ in range(n):
    result_list = reverse_pop_merge(result_list, [int(c) for c in input().split()])  # формируем отсортированный список из n списков

print(*result_list)     # выводим результат
