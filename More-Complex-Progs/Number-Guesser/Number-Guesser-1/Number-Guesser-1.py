from random import randint


def get_max_num():
    print("Введите правую границу диапазона выбора случайного числа")
    while True:
        value = input()
        if not value.isdigit() or not int(value):
            print("Не, введите натуральное число")
            continue
        else:
            return int(value)


def get_num():
    print(f"Отлично, теперь попробуйте угадать число от 1 до {right_limit}")
    while True:
        value = input()
        global attempts_cnt
        attempts_cnt += 1
        if not value.isdigit() or not (1 <= int(value) <= right_limit):
            print(f"Не, надо ввести целое число от 1 до {right_limit}")
            continue
        else:
            return int(value)


def game():
    global attempts_cnt
    attempts_cnt = 0
    attempt = 0
    while attempt != rand_num:
        attempt = get_num()
        attempts_cnt += 1
        if attempt > rand_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif attempt < rand_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
    print("Вы угадали, поздравляем!")
    print(f"Число попыток: {attempts_cnt}\n")


print("Добро пожаловать в числовую угадайку")
while True:
    right_limit = get_max_num()
    rand_num = randint(1, right_limit)
    attempts_cnt = 0
    game()
    print("Желаете сыграть ещё раз? y - да, n - нет")
    if input() == "y":
        continue
    else:
        break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

