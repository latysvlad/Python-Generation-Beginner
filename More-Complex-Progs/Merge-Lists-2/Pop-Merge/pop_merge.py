# put your python code here
def pop_merge(list1, list2):      # функция для объединения двух списков в отсортированный список
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


n = int(input())
result_list = []    # создаем заготовку результирующего списка

for _ in range(n):
    result_list = pop_merge(result_list, [int(c) for c in input().split()])  # в этот раз сразу формируем отсортированный список из n списков

print(*result_list)     # выводим результат
