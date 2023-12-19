def sort_merge(list1, list2):      # функция для объединения двух списков в отсортированный список
    result = (list1 + list2)
    result.sort()
    return result


n = int(input())
result_list = []    # создаем заготовку результирующего списка

for _ in range(n):
    result_list = sort_merge(result_list, [int(c) for c in input().split()])  # формируем отсортированный список из n списков

print(*result_list)     # выводим результат
