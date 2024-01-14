from random import randint


def is_valid(value):    # проверяем, относится ли наше значение вообще к целым числам
    if value.isdigit() and int(value):
        return True
    else:
        return False


def try_input(pointing_message, adjusting_message):   # опционально: либо вводим правую границу диапазона угадайки, либо пытаемся угадать число (тогда считаем число попыток); все это с сообщениями-подсказками
    print(pointing_message, end="")

    while True:
        value = input()
        if flag_start_cnt:    # интересно что здесь он не ругается и не требует объявления глобальной переменной (видимо из-за того что я ее не меняю)
            global tries_cnt
            tries_cnt += 1    # увеличиваем после проверки на флаг начала подсчета попыток

        if not is_valid(value):
            print(adjusting_message)
            continue
        else:
            return int(value)


print("Добро пожаловать в числовую угадайку")
flag_start_cnt = False      # для активации счетчика в функции try_input()
                            # поскольку пока с опциональными параметрами в функциях работать не учили - скорее всего это возможно сделать через классы
while True:
    right_limit = try_input("Введите правую границу диапазона выбора случайного числа\n",
                            'Не, введите натуральное число')
    n = randint(1, right_limit)
    tries_cnt = 0
    flag_start_cnt = True

    print("Отлично, теперь попробуйте угадать число")

    while True:
        attempt = try_input("",
                            f"Не, надо ввести целое число от 1 до {right_limit}")

        if attempt > right_limit:
            print(f"Не, надо ввести целое число от 1 до {right_limit}")
            continue
        elif attempt > n:
            print("Ваше число больше загаданного, попробуйте еще разок")
            continue
        elif attempt < n:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            continue
        else:
            print("Вы угадали, поздравляем!")
            print(f"Число попыток: {tries_cnt}\n")
            break

    print("Желаете сыграть ещё раз? y - да, n - нет")
    if input() == "y":
        continue
    else:
        break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

